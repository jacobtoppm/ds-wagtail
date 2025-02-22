from generic_chooser.widgets import AdminChooser

from .models import RecordPage
from ..ciim.exceptions import KongException


class RecordChooser(AdminChooser):
    choose_one_text = "Choose a record"
    choose_another_text = "Choose another record"
    link_to_chosen_text = "Edit this record"
    model = RecordPage
    choose_modal_url_name = "record_chooser:choose"

    def get_instance(self, pk):
        """Fetch related instance on edit form."""
        try:
            return self.model.search.get(iaid=pk)
        except KongException:
            # If there's a connection issue with Kong, return a stub RecordPage
            # so we have something to render on the ResultsPage edit form.
            return RecordPage(iaid=pk)
