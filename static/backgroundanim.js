const backgroundAnimationList = [
    {
        url: "piupc_82/SB00.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB01.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB02.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB03.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB04.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB05.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB06.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB07.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB08.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB09.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB10.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB11.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB12.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB13.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB14.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB15.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB16.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB17.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB18.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB19.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
    {
        url: "piupc_82/SB20.PNG",
        dx: 0,
        dy: 0,
        dWidth: 640,
        dHeight: 480,
        sx: 0,
        sy: 0,
        sWidth: 256,
        sHeight: 256,
    },
];

const canvas = document.getElementById('bgCanvas');
const ctx = canvas.getContext('2d');

// Load your PNG images
const images = [];
let loadedImagesCount = 0;

// Function to load images
function loadImages() {
    backgroundAnimationList.forEach((data, index) => {
        const img = new Image();
        img.src = data.url;
        img.onload = () => {
            // console.log("image on load", img)
            backgroundAnimationList[index].img = img
            loadedImagesCount++;
            if (loadedImagesCount === backgroundAnimationList.length) {
                requestAnimationFrame(animate);
            }
        };
    });
}

// Animation variables
let currentIndex = 0;
const frameRate = 60; // Adjust for speed
const changeInterval = 100; // Change image every 2 seconds
let lastChangeTime = 0;


// Animation function
function animate(timestamp) {
    const totalImages = backgroundAnimationList.length;
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Update the image based on time
    if (timestamp - lastChangeTime >= changeInterval) {
        // console.log("pasó el interval?")
        currentIndex = (currentIndex + 1) % totalImages; // Loop through images
        lastChangeTime = timestamp;
    }

    // Draw the current image
    const { img, dx, dy, dWidth, dHeight, sx, sy, sWidth, sHeight } = backgroundAnimationList[currentIndex];
    // console.log('image', images[currentIndex])

    ctx.drawImage(img, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);

    requestAnimationFrame(animate);
}

// Start loading images
loadImages();
