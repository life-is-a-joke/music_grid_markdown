import os

from mkdocs import plugins

from .renderrer import render_md_html, update_toc_readme, get_css


def get_relpath_from_docs_path(p):
    return os.path.join(os.getcwd(), 'docs', p)


index_filename = 'index.md'


class MusicGridPlugin(plugins.BasePlugin):

    @staticmethod
    def is_mmd_page(page):
        return page.file.src_uri.startswith('music/') and \
               not page.file.src_uri.endswith('/' + index_filename)

    def on_page_markdown(self, markdown, page, config, files):
        if self.is_mmd_page(page):
            with open(page.file.abs_src_path, 'r') as f:
                mmd = f.readlines()
                markdown = render_md_html(mmd)
        return markdown

    def on_post_page(self, output, page, config):
        if self.is_mmd_page(page):
            css = get_css()
            output += f'<style>{css}</style>'

        return output
