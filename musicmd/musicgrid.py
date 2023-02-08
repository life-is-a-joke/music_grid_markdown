import os

from mkdocs import plugins

from .renderrer import render_md_html, update_toc_readme


def get_relpath_from_docs_path(p):
    return os.path.join(os.getcwd(), 'docs', p)


index_filename = 'index.md'


class MusicGridPlugin(plugins.BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        if page.file.src_uri.startswith('music/'):
            if not page.file.src_uri.endswith('/' + index_filename):
                with open(page.file.abs_src_path, 'r') as f:
                    mmd = f.readlines()
                    markdown = render_md_html(mmd)
        return markdown
