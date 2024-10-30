from typing import Any

from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.callbacks import BaseCallbackHandler

import utils
import streamlit as st

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.tools import GoogleSearchRun
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain.agents import AgentExecutor, create_react_agent, initialize_agent, AgentType
from langchain_core.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain_core.runnables.history import RunnableWithMessageHistory

from streaming import StreamHandler

st.set_page_config(page_title="ChatNet", page_icon="🌐")
st.header('Chatbot Mark-One 🤖')

class QuietCallbackHandler(BaseCallbackHandler):
    def __init__(self, streamHandler):
        self.streamHandler = streamHandler

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.streamHandler.on_llm_new_token(token)

    def on_agent_action(self, action: AgentAction, **kwargs) -> Any:
        pass  # Suppress agent action messages

    def on_agent_finish(self, finish: AgentFinish, **kwargs) -> Any:
        pass  # Suppress finish messages


class ContextChatbot:
    def __init__(self):
        utils.sync_st_session()
        self.llm = utils.configure_llm()
        if "agent_state" not in st.session_state:
            st.session_state.agent_state = None

    def setup_google_search(self) -> Tool:
        search = GoogleSearchAPIWrapper(
        )

        return Tool(
            name="Google Search",
            description="Search Google for recent information about a topic",
            func=search.run
        )

    def setup_agent(self):
        # Only create a new agent if one doesn't exist
        if st.session_state.agent_state is None:
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            search_tool = self.setup_google_search()

            agent = initialize_agent(
                tools=[search_tool],
                llm=self.llm,
                agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
                memory=memory,
                verbose=False  # Set verbose to False to reduce output
            )

            st.session_state.agent_state = agent

        return st.session_state.agent_state

    @utils.enable_chat_history
    def main(self):
        agent = self.setup_agent()
        user_query = st.chat_input(placeholder="Ask me anything!")

        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                # Use the custom callback handler to suppress chain messages
                quiet_cb = QuietCallbackHandler(st_cb)

                try:
                    response = agent.run(
                        input=user_query,
                        callbacks=[quiet_cb]
                    )
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    utils.print_qa(ContextChatbot, user_query, response)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    if "agent_state" in st.session_state:
                        # Reset agent state on error
                        st.session_state.agent_state = None


if __name__ == "__main__":
    obj = ContextChatbot()
    obj.main()
