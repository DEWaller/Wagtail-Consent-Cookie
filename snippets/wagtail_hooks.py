# from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
# from .models import HeaderTitle

# class HeaderTitleAdmin(ModelAdmin):
#     model = HeaderTitle
#     menu_label = 'Header title'  # How the snippet will appear in the admin menu
#     menu_icon = 'snippet'  # Choose an icon for your snippet
#     menu_order = 200  # Set the order in the admin menu
#     add_to_settings_menu = False  # Whether to add your snippet to the Settings menu
#     exclude_from_explorer = False  # Whether to hide the snippet from the Explorer menu
#     list_display = ('title',)  # Fields to display in the admin list view

# # Register the MySnippetAdmin class with the modeladmin_register
# modeladmin_register(HeaderTitleAdmin)   