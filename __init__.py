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
                    'default': 'C:\\Ember Media Manager BETA\\Ember Media Manager.exe',
                },
                {
                    'name': 'app_args',
                    'label': 'Custom Command Line Arguments',
                    'advanced': True,
                    'default': '-newauto -all -nowindow',
                    'description': 'Choose your custom command line arguments to call Ember Media Manager, separated by <space>',
                },
            ],
        }
    ],
}]        