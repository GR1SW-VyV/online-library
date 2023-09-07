def before_scenario(context, scenario):
    print("shark")
    if 'documents_setup' in scenario.feature.tags:
        context.document = dict()
