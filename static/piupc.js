
const adre = [
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 230,
    dy: 367,
    dWidth: 89,
    dHeight: 31,
    sx: 167,
    sy: 104,
    sWidth: 256,
    sHeight: 135,
  },
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 319,
    dy: 370,
    dWidth: 68,
    dHeight: 30,
    sx: 255,
    sy: 135,
    sWidth: 187,
    sHeight: 165,
  },
];

const logo01 = [
  {
    url: "piupc_82/LOGO03.PNG",
    dx: 151,
    dy: 74,
    dWidth: 256,
    dHeight: 211,
    sx: 0,
    sy: 0,
    sWidth: 256,
    sHeight: 211,
  },
  {
    url: "piupc_82/LOGO04.PNG",
    dx: 407,
    dy: 186,
    dWidth: 73,
    dHeight: 106,
    sx: 0,
    sy: 112,
    sWidth: 73,
    sHeight: 218,
  },
];

const logo02 = [
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 406,
    dy: 73,
    dWidth: 88,
    dHeight: 256,
    sx: 0,
    sy: 0,
    sWidth: 88,
    sHeight: 256,
  },
  {
    url: "piupc_82/LOGO01.PNG",
    dx: 150,
    dy: 73,
    dWidth: 256,
    dHeight: 256,
    sx: 0,
    sy: 0,
    sWidth: 256,
    sHeight: 256,
  },
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 90,
    dy: 329,
    dWidth: 120,
    dHeight: 21,
    sx: 96,
    sy: 5,
    sWidth: 216,
    sHeight: 26,
  },
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 206,
    dy: 332,
    dWidth: 103,
    dHeight: 23,
    sx: 100,
    sy: 30,
    sWidth: 203,
    sHeight: 53,
  },
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 307,
    dy: 332,
    dWidth: 139,
    dHeight: 18,
    sx: 105,
    sy: 55,
    sWidth: 244,
    sHeight: 73,
  },
  {
    url: "piupc_82/LOGO02.PNG",
    dx: 440,
    dy: 331,
    dWidth: 110,
    dHeight: 17,
    sx: 102,
    sy: 78,
    sWidth: 212,
    sHeight: 95,
  },
];

const fillCanvas = (sprite) => {
  const { url, dx, dy, dWidth, dHeight, sx, sy, sWidth, sHeight } = sprite;
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");
  var img = new Image();
  img.addEventListener("load", () => {
    ctx.drawImage(img, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);
  });
  img.src = url;
};

const fillLogo = () => {
  // logo01.forEach((item) => {
  //   fillCanvas(item);
  // });

  logo02.forEach((item) => {
    fillCanvas(item);
  });

  adre.forEach(item => {
    fillCanvas(item)
  })
};
