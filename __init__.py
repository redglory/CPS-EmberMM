from .main import EmberMediaManager

def autoload():
	return EmberMediaManager()


config = [{
    'name': 'embermediamanager',
    'groups': [
        {
            'tab': 'notifications',
            'list': 'notification_providers',
            'name': 'embermediamanager',
            'label': 'Ember Media Manager',
            'description': 'Ember Media Manager 1.3.20+ versions',
            'options': [
                {
                    'name': 'enabled',
                    'default': 0,
                    'type': 'enabler',
                },
                {
                    'name': 'app_path',
                    'label': 'Application Path',
                    'type': 'directory',
                    'description': 'Choose your Ember Media Manager application path',
                },
                {
                    'name': 'update_library',
                    'default': False,
                    'label': 'Update library',
                    'type': 'bool',
                    'advanced': True,
                    'description': 'Update and scrape new movies instead of just downloaded movie',
                },
                {
                    'name': 'custom_profile',
                    'label': 'Run Ember using specific profile',
                    'advanced': True,
                    'default': '',
                    'description': 'Use this parameter if you want to run Ember Media Manager with specified profile',
                },
                {
                    'name': 'scrape_args',
                    'label': 'Scraping arguments',
                    'advanced': True,
                    'default': 'newauto all -nowindow',
                    'description': 'Set your custom scraping arguments',
                },
            ],
        }
    ],
}]        