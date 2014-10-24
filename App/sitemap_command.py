import yaml, os, time
from  screenshotter import Screenshotter


class SitemapCommand:
    def __init__( self, args ):
        self.data = yaml.safe_load(file(args.config_file))
        self.screenshotter = Screenshotter()

        base_path = os.path.join( args.destination, self.data['project_name'] )
        self.sitemapper(self.data, base_path )
        self.screenshotter.close()
        print "Sitemap captured."
        print "="*50


    def make_file( self, path, file_name, url):
        the_file = path + "/" + "_" + file_name +"_log.txt" # added the "_" to make file appear first alphabetically
        target = open(the_file, 'a')

        now = time.strftime("%c")
        time_stamp = " File created: " + time.strftime("%c")

        file_contents = time_stamp + "\n URL: " + url + "\n\n"

        target.write(file_contents)
        target.close()


    def make_folder( self, path):
        if not os.path.exists(path):
                os.makedirs(path)
                print path + ".dir created."


    def screenshot_state( self, page, folder, state ):
        file_name = page['name'] + '-' + '-' + state['name'] + '.png'
        file_path = os.path.join( folder, file_name )
        if self.screenshotter.click_selector(state['enter']):
            self.screenshotter.take_screenshot( file_path )
            print "Saving state screenshot: " + file_name
            if 'leave' in state:
                self.screenshotter.click_selector(state['leave'])


    def handle_url( self, page, folder ):
        file_name = page['name'] + '-' + '.png'
        file_path = os.path.join( folder, file_name )
        self.make_folder( folder )
        self.screenshotter.get_url( page['url'] )
        self.screenshotter.take_screenshot( file_path )
        print "Saving page screenshot: " + file_name

        if 'states' in page:
            for state in page['states']:
                self.screenshot_state( page, folder, state )

        if 'actions' in page:
            self.handle_actions( page, folder, page['actions'] )


    def handle_actions( self, page, folder, actions ):
        for action in actions:
            if ( action['type'] == 'click' ):
                self.screenshotter.click_selector(action['selector'])
            if ( action['type'] == 'screenshot' ):
                file_name = page['name'] + '-' + '-' + action['name'] + '.png'
                file_path = os.path.join( folder, file_name )
                print "Saving state screenshot: " + file_name
                self.screenshotter.take_screenshot(file_path)


    def sitemapper( self, pages, prefix):
        if not 'subpages' in pages:
            return 0
        for page in pages['subpages']:
            folder = os.path.join( prefix, page['name'] )
            if 'url' in page:
                self.handle_url( page, folder )
            if 'subpages' in page:
                self.sitemapper( page, folder )
