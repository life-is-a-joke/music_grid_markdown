import os

from mkdocs import plugins

from .renderrer import render_md_html


def get_relpath_from_docs_path(p):
    return os.path.join(os.getcwd(), 'docs', p)


class MusicGridPlugin(plugins.BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        if page.file.src_uri.startswith('music/'):
            if page.file.src_uri.endswith('/README.md'):
                markdown = '<p>Music files</p>'
                p = get_relpath_from_docs_path(page.file.src_uri[:-len('/README.md')])

                for fn in os.listdir(p):
                    print(fn)
                    if fn.endswith('README.md'):
                        continue
                    if fn.endswith('.md'):
                        markdown += f'<p>{fn}</p>'
                        files.append()
            else:
                with open(page.file.abs_src_path, 'r') as f:
                    mmd = f.readlines()
                    markdown = render_md_html(mmd)
        return markdown
