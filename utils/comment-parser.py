import click
import csv
import os
import yaml

@click.command()
@click.argument("filename")
def main(filename):
    comments = []
    fields = ['timestamp','author_name','author_email', 'comment_text','slug']
    with open(filename, 'r') as f:
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


if __name__ == '__main__':
    main()
