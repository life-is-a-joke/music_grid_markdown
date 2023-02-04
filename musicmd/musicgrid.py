from mkdocs import plugins

from .musicmd.renderrer import render_md_html


class MusicGridPlugin(plugins.BasePlugin):

    def on_page_markdown(self, markdown, page, config, files):
        if page.file.src_uri.startswith('music/'):
            if page.file.src_uri.endswith('/README.md'):
                markdown = '<p>Music files</p>'
                p = page.file.src_uri[:len('/README.md')]
                for f in files:
                    print(f.src_uri)
                    if f.src_uri.startswith(p):
                        markdown += f'<p>{f.src_uri}</p>'
            else:
                with open(page.file.abs_src_path, 'r') as f:
                    mmd = f.readlines()
                    markdown = render_md_html(mmd)
        return markdown
