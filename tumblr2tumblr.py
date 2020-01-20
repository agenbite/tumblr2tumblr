import oauth2
import pytumblr

OLDBLOG = "name_of_the_source_blog"
NEWBLOG = "name_of_the_destination_blog"

# Authenticate via OAuth
# https://www.tumblr.com/docs/en/api/v2#authentication
client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)

noPosts = client.blog_info(OLDBLOG)["blog"]["posts"]

for i in range(noPosts-1, 0, -1):
    post = client.posts(OLDBLOG, offset=i, limit=1)["posts"][0]

    if post["type"] != "text":
        continue

    if not post["title"]:
        print(i, "(sin título)"), post["tags"]

        client.create_text(NEWBLOG,
                           state="published",
                           slug=post["slug"],
                           title=" ",
                           body=post["body"],
                           date=post["date"],
                           tags=post["tags"])
    else:
       print(i, post["title"], post["tags"])

       client.create_text(NEWBLOG,
                           state="published",
                           slug=post["slug"],
                           title=post["title"],
                           body=post["body"],
                           date=post["date"],
                           tags=post["tags"])
