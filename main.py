from subprocess import Popen, PIPE
import os
import time
import traceback

from couchpotato.core.logger import CPLog
from couchpotato.core.event import addEvent, fireEvent
from couchpotato.core.helpers.variable import splitString
from couchpotato.core.plugins.base import Plugin
from couchpotato.environment import Env


log = CPLog(__name__)


class EmberMediaManager(Plugin):

    def __init__(self):

        if self.conf('enabled'): # only load plugin if it is enabled on configs
            # check if development setting is enabled to load new code and trigger renamer automatically
            if Env.get('dev'):
                def test():
                    fireEvent('renamer.scan')
                addEvent('app.load', test)

            addEvent('renamer.after', self.run_ember, priority=90)

    ###########################################
    #### Ember Media Manager Auto Scraping ####
    ###########################################
    ### Command line parameters
    ### -------------
    ### -addmoviesource
    ### -addtvshowsource
    ### -cleanvideodb
    ### -run
    ### -scanfolder
    ### -scrapemovies
    ###     # ScrapeType for -scrapemovies
    ###     allask
    ###     allauto
    ###     allskip
    ###     markedask
    ###     markedauto
    ###     markedskip
    ###     missingask
    ###     missingauto
    ###     missingskip
    ###     newask
    ###     newauto
    ###     newskip
    ### -scrapetvshows
    ###     # ScrapeType for -scrapetvshows
    ###     allask
    ###     allauto
    ###     allskip
    ###     markedask
    ###     markedauto
    ###     markedskip
    ###     missingask
    ###     missingauto
    ###     missingskip
    ###     newask
    ###     newauto
    ###     newskip
    ### --verbose
    ### -nowindow
    ### -updatemovies
    ### -updatetvshows
    ###########################################
    def run_ember(self, message=None, group=None):

        # Ember Media Manager installation path
        app_path = os.path.join(self.conf('app_path'), 'Ember Media Manager.exe')
        # Command Line Parameters
        app_args = splitString(self.conf('app_args'), ' ')

        # Fallback to default parameters if empty
        if len(app_args) == 0:
            app_args.append('-updatemovies')
            app_args.append('-scrapemovies')
            app_args.append('newauto')
            app_args.append('all')
            app_args.append('-nowindow')

        command = []
        command.append(app_path)
        for arg in app_args:
            command.append(arg)

        # Lauch Ember Media Manager
        startTime = time.time()
        log.info("Starting Ember Media Manager with application arguments: %s", str(command))
        log.debug("IMDB identifier: %s", group['identifier'])
        log.debug("Movie name: %s", group['dirname'])
        log.debug("Downloaded Movie directory: %s", group['parentdir'])

        try:
            p = Popen(command, stdout=PIPE)
            log.info("Ember Media Manager: running on PID: (" + str(p.pid) + ")")
            res = p.wait()
            if res == 0:
                endTime = time.time()
                log.info("Ember Media Manager ran sucessfully for: %s seconds", str(int(endTime - startTime)))
                return True
            else:
                log.info("Ember Media Manager returned an error code: %s \n %s", (str(res), (traceback.format_exc())))
        except:
            log.error("Failed to call Ember Media Manager: %s", (traceback.format_exc()))

        return False
