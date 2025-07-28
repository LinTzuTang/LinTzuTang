from scholarly import scholarly
import datetime

SCHOLAR_ID = "2Yxesf0AAAAJ"

author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author, sections=["indices"])  # 只填 h-index 和 citation

# 嘗試取得 publications 總數
paper_count = len(author.get("publications", []))
if paper_count == 0:
    paper_count = "N/A"

name = author["name"]
h_index = author["hindex"]
citations = author["citedby"]
date = datetime.datetime.now().strftime("%Y-%m-%d")

block = f"""<!--GS_START-->
📚 **Google Scholar Statistics**
- 👨‍🔬 Name: {name}
- 🧠 h-index: {h_index}
- 📄 Total Publications: {paper_count}
- 📈 Total Citations: {citations}
- 🔗 [View on Google Scholar](https://scholar.google.com/citations?user={SCHOLAR_ID})
_Last updated: {date}_
<!--GS_END-->"""

with open("README.md", "r") as f:
    content = f.read()

start = content.find("<!--GS_START-->")
end = content.find("<!--GS_END-->") + len("<!--GS_END-->")

if start != -1 and end != -1:
    new_content = content[:start] + block + content[end:]
    with open("README.md", "w") as f:
        f.write(new_content)
