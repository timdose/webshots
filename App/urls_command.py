import os
import time
import yaml
from datetime import datetime
from selenium import webdriver

class UrlsCommand:
    def __init__(self, args):
        self.args = args
        self.start_time = None
        self.verbose = args.verbose
    
        self.config = yaml.load(file(args.config_file))

        self.output_folder = os.path.join( args.destination, self.get_timestamp() )
        
        self.urls = self.config['urls']
        
        self.max_permutations = len(self.urls)

        self.go()
        
    
    def set_max_permutations(self, max ):
        self.max_permutations = int(max);

    
    def go(self):
        self.start_time = datetime.now()
        self.take_screenshots( self.urls, self.output_folder )
        self.report_completion()
        
        
    def take_screenshots(self ,urls, output_folder):
        if not os.path.isdir(output_folder):
             os.makedirs(output_folder)

        driver = webdriver.Firefox()
        driver.set_window_size( 1200, 700 );

        for url in urls[0:self.max_permutations]:
            screenshot_name = self.get_screenshot_filename_from_url( url )
            screenshot_dest = os.path.join( output_folder, screenshot_name )
            
            if self.verbose:
                print url
                
            driver.get(url)

            time.sleep(2)

            driver.save_screenshot(screenshot_dest)

        driver.quit()
        

    def get_screenshot_filename_from_url( self, url ):
        return url.replace('http://', '').replace('https://', '').replace('/','__') + '.png'


    def get_timestamp(self):
        ts = time.time()
        return datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

        
    def report_completion(self):
        time_elapsed = datetime.now() - self.start_time
        print 'took screenshots of ' + str(self.max_permutations) + ' permutations in ' + str(time_elapsed)