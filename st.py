import streamlit as st
import time

# def bot_print(content, avatar: str = "🤖"):
#     re = ''
#     with st.chat_message("assistant", avatar=avatar):
#         message_placeholder = st.empty()
#         full_response = ""
#         for chunk in content.split():
#             full_response += chunk + " "
#             time.sleep(0.05)
#             message_placeholder.markdown(full_response + "▌")
#         data = full_response.split(' ')
#         re = "\n".join(data)
#         # for d in data:
#         #     d = d + '\n'
#         #     re += d
#         print('re:',re)
#         message_placeholder.markdown(re)





# 可以使用三引号来多行输入 Markdown 格式的文本
markdown_text = """
### 这是一个三级标题

这是一个包含列表的文本：
- 列表项 1
- 列表项 2
- 列表项 3
"""

data = ["我", "哎", "额外"]
re = ''
# for d in data:
#     d = d + "\n"
#     re += d

# for d in data:
#     d = d + "<br />"
#     re += d

# for d in data:
#     d = d + "\r\n"
#     re += d

re = "  \n".join(data)
print(re)

st.markdown(re)