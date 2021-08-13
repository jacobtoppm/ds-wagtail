import manage_details_element from './modules/manage_details_element';
import scroll_to_bottom from "./scroll_to_bottom";

const summary_element = document.querySelector('#js-hierarchy-global summary');
const hierarchy_list = document.querySelector('.hierarchy-global__list');

scroll_to_bottom(hierarchy_list);

summary_element.addEventListener('click', e => {

    if (window.innerWidth < 1200) {
        return;
    }
    e.preventDefault();
});

document.addEventListener("DOMContentLoaded", () => {
    manage_details_element();
});

window.addEventListener("resize", () => {
    manage_details_element();
});
