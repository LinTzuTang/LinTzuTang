from scholarly import scholarly
import datetime
import re

SCHOLAR_ID = "2Yxesf0AAAAJ"

author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author, sections=["indices"])

h_index = author["hindex"]
citations = author["citedby"]
i10_index = author.get("i10index", "N/A")
date = datetime.datetime.now().strftime("%Y-%m-%d")

with open("README.md", "r") as f:
    content = f.read()

# Preserve existing publication count
pub_match = re.search(r"📄 Total Publications: (\d+)", content)
pub_text = f"- 📄 Total Publications: {pub_match.group(1)}" if pub_match else ""

block = f"""<!--GS_START-->
📚 **Google Scholar Statistics**
- 📈 Total Citations: {citations}
- 🧠 h-index: {h_index}
- 🏅 i10-index: {i10_index}
{pub_text}
_Last updated: {date}_
<!--GS_END-->"""

start = content.find("<!--GS_START-->")
end = content.find("<!--GS_END-->") + len("<!--GS_END-->")

if start != -1 and end != -1:
    new_content = content[:start] + block + content[end:]
    with open("README.md", "w") as f:
        f.write(new_content)
