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

(function () {

    let bg;
    let bgImage;
    let canvas;

    function bgLoop() {
        window.requestAnimationFrame(bgLoop);

        bg.update();
        bg.render();
    }

    function backgroundAnimation(options) {

        var that = {},
            frameIndex = 0,
            tickCount = 0,
            ticksPerFrame = options.ticksPerFrame || 0;
        that.animationList = options.animationList;
        that.numberOfFrames = that.animationList.length;
        that.context = options.context;
        that.sprite = options.sprite;

        that.update = function () {

            tickCount += 1;

            if (tickCount > ticksPerFrame) {

                tickCount = 0;

                // If the current frame index is in range
                if (frameIndex < that.numberOfFrames - 1) {
                    // Go to the next frame
                    frameIndex += 1;
                } else {
                    frameIndex = 0;
                }
            }
        };

        that.render = function () {
            const { url, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight } = that.animationList[frameIndex];

            // Clear the canvas
            that.context.clearRect(0, 0, 640, 480);
            bgImage.src = url;
            that.context.drawImage(bgImage, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
            console.log("bgimage src", bgImage.src)
        };

        return that;
    }

    // Get canvas
    canvas = document.getElementById("bgCanvas");

    // Create sprite sheet
    bgImage = new Image();

    // Create sprite
    bg = backgroundAnimation({
        context: canvas.getContext("2d"),
        animationList: backgroundAnimationList,
        ticksPerFrame: 10
    });

    // Load sprite sheet
    bgImage.addEventListener("load", bgLoop);
    bgImage.src = backgroundAnimationList[0].url;

}());