import push_to_data_layer from "./push_to_data_layer";

let stored_percentage;

const audio_tracking = () => {

    const event_handler = (e) => {

        let filename;

        try {
            filename = e.target.getElementsByTagName('source')[0].getAttribute('src');
        } catch (e) {
            console.error(e);
            filename = 'Not found'
        }

        switch (e.type) {

            case 'timeupdate':

                const percentage = Math.floor((Math.floor(e.target.currentTime) / Math.floor(e.target.duration)) * 100);

                if (stored_percentage === percentage) {
                    return;
                }

                if (percentage === 0) {
                    return;
                }

                if (percentage % 5 !== 0) {
                    return;
                }

                stored_percentage = percentage;

                push_to_data_layer({
                    'media_type': 'audio',
                    'data_media_controls': 'progress',
                    'data_media_title': `Filename: ${filename}`,
                    'data_progress': `${percentage}% played`
                });

                break;

            case 'play':

                push_to_data_layer({
                    'media_type': 'audio',
                    'data_media_controls': 'play',
                    'data_media_title': `Filename: ${filename}`,
                    'data_media_length': `Length of audio ${Math.floor(e.target.duration)} seconds`
                });

                break;

            case 'pause':

                push_to_data_layer({
                    'data_media_title': `Filename: ${filename}`,
                    'data_media_controls': 'pause',
                    'data_audio_value': `Paused at ${Math.floor(e.target.currentTime)} seconds`
                });

                break;

            case'ended':

                push_to_data_layer({
                    'data_media_title': `Filename: ${filename}`,
                    'data_media_controls': 'ended'
                });

                break;

            default:
                break;
        }
    };

    const audios = document.querySelectorAll('audio[controls]');

    for (let i = 0; i < audios.length; i++) {

        audios[i].addEventListener('play', event_handler, false);
        audios[i].addEventListener('pause', event_handler, false);
        audios[i].addEventListener('ended', event_handler, false);
        audios[i].addEventListener('timeupdate', event_handler, false);
    }
};

export default audio_tracking;
