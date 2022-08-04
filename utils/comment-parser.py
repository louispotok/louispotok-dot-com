import click
import csv
import datetime
import os
import yaml


@click.group()
def cli():
    pass

@cli.command()
@click.argument("filename")
def wordpress(filename):
    """
    Parses comments, as exported from a wordpress database, into the YML format this repo expects.
    """
    comments = []
    fields = ['timestamp','author_name','author_email', 'comment_text','slug']
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            comments.append({k:row[k] for k in fields})
    for c in comments:
        slug_path = os.path.join('_data/comments/', c['slug'])
        comment_path = os.path.join(slug_path, f"comment-{c['timestamp']}.yml")
        if not os.path.exists(slug_path):
            os.mkdir(slug_path)
        if not os.path.exists(comment_path):
            with open(comment_path, 'w') as f:
                yaml.dump(c, f)

def iso8601_to_timestamp(s):
    """
    "2022-08-03T19:04:16.075Z" -> 1659528256
    """
    return round(datetime.datetime.fromisoformat(s[:-1]).timestamp())

@cli.command()
@click.argument("filename")
def netlify(filename):
    """
    Parses comments, as exported from a wordpress database, into the YML format this repo expects.

    Example csv:
        "slug","name","email","message","ip","user_agent","referrer","created_at"
        "setting-up-matomo","Aman","","Thanks for sharing all this. I came to check which tutorials you used. The second one you linked to is a dead link, from ""Art of Adventuring"" . ","147.219.160.3","UA_STRING","https://www.louispotok.com/2021/02/13/setting-up-matomo.html","2022-08-03T19:04:16.075Z"
    """
    comments = []
    identity = lambda x: x
    fields = [
            # source_field_name, dest_field_name, mapping_fn
            ("created_at", "timestamp", iso8601_to_timestamp),
            ("name", "author_name", identity),
            ("email",'author_email', identity),
            ("message",'comment_text', identity),
            ('slug', 'slug', identity)
            ]
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        source_fields = [x[0] for x in fields]
        assert set(source_fields).issubset(reader.fieldnames)
        for row in reader:
            comment = {}
            for f in fields:
                src_name, dest_name, fn = f
                comment[dest_name] = fn(row[src_name])
            comments.append(comment)
    for c in comments:
        slug_path = os.path.join('_data/comments/', c['slug'])
        comment_path = os.path.join(slug_path, f"comment-{c['timestamp']}.yml")
        if not os.path.exists(slug_path):
            os.mkdir(slug_path)
        if not os.path.exists(comment_path):
            with open(comment_path, 'w') as f:
                yaml.dump(c, f)


if __name__ == '__main__':
    cli()
