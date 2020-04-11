---
title: "How to Automate Markdown"
date: 2020-04-11
tags: [Projects]
---

##### please see link for code
[Project Link](https://github.com/cullinap/automate-markdown-)

### How to Automate Markdown

Making a markdown file is a necessary evil, but not the most rewarding task. I would rather write code than re-google how to format a link when it comes time to document my code. Of course this brings up an excellent opportunity to automate this task. In fact I am writing this post using my template code which removes my excuse for not doing it. 

The general architecture of the program consists of a shell script that runs a python script. Of course I could just call a python script to do this, but I think it makes it a bit simpler this way. The shell script takes three inputs: post name, tag, and link. For this example the inputs are setup to feed a template for my github.io website. The bash script checks to see if the file exists and if not it calls the python script while feeding arguments to it. Another feature I wanted was to add today's date which of course is captured in the first link and fed into the python script.

```bash
today=$(date +%Y-%m-%d)

echo "making new blog post, enter a name:"
read -r -p 'post name: ' desc
read -r -p 'tags: ' tag
read -r -p 'link: ' link

# TEMPLATE=_posts/template.md
FILE=_posts/$today-$desc.md

if test -f "$FILE"; then
        echo "file exists"
else
        echo "making file: $today-$desc"
        python3 _posts/make_file.py $today $tag $link $desc
        echo "file made"
fi
```

The python script takes the arguments slightly backwards from how it was entered in the shell script, but I felt the interface from shell seemed more intuitive and that is why wrote it the way I did. Date, tags, links, and args (title) are fed into the function where they are assigned to the proper variable. These variables are fed into a dictionary that creates the template lines.

It took me a second to figure this one out, but I finally figured out I needed a f-string to create the proper output in the markdown file. All that information is fed into the with-statement where I iterate line by line thorugh the dictionary to create the file. 

```python
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
```


