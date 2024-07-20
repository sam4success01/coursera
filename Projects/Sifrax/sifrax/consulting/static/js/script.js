const videos = [
    { src: 'static/media/1.mp4', text: 'We take pride in ensuring your satisfaction' },
    { src: 'static/media/2.mp4', text: 'We align your goals with your vision' },
    { src: 'static/media/3.mp4', text: 'We offer solution to your business challenges' },
    { src: 'static/media/4.mp4', text: 'We design successful strategies to achieve your business goals' },
    { src: 'static/media/5.mp4', text: 'We have the best team for your projects' }
];
let currentVideo = 0;

const videoElement = document.getElementById('video-bg');
const textOverlay = document.querySelector('.overlay');

function changeVideo() {
    videoElement.style.opacity = 0;
    setTimeout(() => {
        currentVideo = (currentVideo + 1) % videos.length;
        videoElement.src = videos[currentVideo].src;
        textOverlay.innerText = videos[currentVideo].text;
        videoElement.play();
        videoElement.style.opacity = 1;
    }, 0);
}

videoElement.addEventListener('ended', changeVideo);

// Adjusted to properly cycle through videos without immediately repeating
setInterval(changeVideo, 5000);  // Ensuring video runs for the length it's supposed to.



