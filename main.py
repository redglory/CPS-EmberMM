from subprocess import Popen, PIPE
import time
import traceback

from couchpotato.core.logger import CPLog
from couchpotato.core.event import addEvent, fireEvent
from couchpotato.core.plugins.base import Plugin
from couchpotato.environment import Env


log = CPLog(__name__)


class EmberMediaManager(Plugin):

    def __init__(self):

        # check if development setting is enabled to load new code and trigger renamer automatically
        if Env.get('dev'):
            def test():
                fireEvent('renamer.scan')
            addEvent('app.load', test);

        addEvent('renamer.after', self.run_ember, priority = 90)
        
    ###########################################
    #### Ember Media Manager Auto Scraping ####
    ###########################################
    ### Command line parameters
    ### -------------
    ### -fullask
    ### -fullauto
    ### -missask
    ### -missauto
    ### -newask
    ### -newauto
    ### -markask
    ### -markauto
    ### -file
    ### -folder
    ### -export
    ### -template
    ### -resize
    ### -all
    ### -nfo
    ### -posters
    ### -fanart
    ### -extra
    ### -nowindow
    ### -run
    ###########################################
    def run_ember(self, message = None, group = None):
        # Ember Media Manager installation path
        app_path = self.conf('app_path', default = 'C:\\Ember Media Manager BETA\\Ember Media Manager.exe') #['D:\\EmberMediaManager\\Ember Media Manager.exe']
        # Command Line Parameters
        app_args = splitString(self.conf('app_args'), ' ')
        # Fall back to default parameters if empty
        if len(app_args) == 0:
            app_args.append('-newauto')
            app_args.append('-all')
            app_args.append('-nowindow')
        
        command.append(app_path)
        command.append(app_args)

        # Lauch Ember Media Manager
        startTime = time.time()
        log.info("Start scrapping with Ember Media Manager with application arguments: %s", str(command))
        log.debug("IMDB identifier: %s", group['identifier']) # IMDB identifier
        log.debug("Movie name: %s", group['dirname']) # Movie name
        log.debug("Downloaded Movie directory: %s", group['parentdir']) # Download movie directory
        
        try:
            p = Popen(command, stdout=PIPE)
            log.info("Ember Media Manager: running on PID: (" + str(p.pid) + ")")
            res = p.wait()
            if res == 0:
                endTime = time.time()
                log.info("Ember Media Manager ran sucessfully for: %s seconds", str(int(endTime - startTime)))
                #group['ember_ok'] = True
                #log.debug("group['ember_ok'] = %s", group['ember_ok'])
                #log.debug("sleeping for 10 seconds...")
                #time.sleep(10)
                return True
            else:
                log.info("Ember Media Manager returned an error code: %s", str(res))
        except:
            log.error("Failed to call Ember Media Manager: %s", (traceback.format_exc()))

        return False