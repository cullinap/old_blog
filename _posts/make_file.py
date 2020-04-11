import os
import sys

LINE = f"---"

def main(date, tags, link, *title):

    blog_title  = f'{" ".join([t for t in title])}'
    date        = f"{date}"
    tags        = f"{tags}"
    link        = f"{link}"
    
    vals = {
        1: LINE,
        2: f'title: "{blog_title}"',
        3: f"date: {date}",
        4: f"tags: [{tags}]",
        5: LINE,
        6: "",
        7: f"# please see link for code",
        8: f"[Project Link]({link})",
        9: "",
        10: f"# {blog_title}",
        11: "",
        12: f"```python",
        13: f"code example",
        14: f"```"
    }

    file_name = "_posts/" + date + "-" + "-".join(list(title))

    with open(f'{file_name}.md', mode='w') as md_file:
        for v in vals.values():
            md_file.write(v + "\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], *sys.argv[4:])


