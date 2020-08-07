const colorPatterns = {
        steelblue: {
            primary: "steelblue",
            secondary: "#85C1E9",
            highlight: "#FFEB3B",
            text: "white",
            caption: "lightgrey"
        },
        lightseagreen: {
            primary: "lightseagreen",
            secondary: "#008080",
            highlight: "#FFEB3B",
            text: "white",
            caption: "lightgrey"
        },
        darkslategray: {
            primary: "darkslategray",
            secondary: "#00AD83",
            highlight: "#FFEB3B",
            text: "white",
            caption: "lightgrey"
        },
        palevioletred: {
            primary: "palevioletred",
            secondary: "#FBB0B0",
            highlight: "#FFEB3B",
            text: "white",
            caption: "lightgrey"
        }
    };

const colorPickers = document.querySelectorAll('.color-picker');
// alert(colorPickers.length);
const changeColor = function(e) {
    const id = $(this).attr('id');
    const body = document.querySelector('body');
    // if (!isDark(id)) {
        // should also change nav's color and text color
    // }

    // remove 'selected' class for previous color picker
    if(body.style.getPropertyValue('--primary')){
        const oldColor = "#" + body.style.getPropertyValue('--primary');
        const oldColorPicker = $(oldColor);
        oldColorPicker.removeClass('selected');
    }



    // change variables in body and add 'selected' class
    const pattern = colorPatterns[id];
    body.style.setProperty('--primary', pattern.primary);
    body.style.setProperty('--secondary', pattern.secondary);
    body.style.setProperty('--highlight', pattern.highlight);
    body.style.setProperty('--text', pattern.text);
    body.style.setProperty('--caption', pattern.caption);
    $(this).addClass('selected');
};

for (let i = 0; i < colorPickers.length; i++) {
    const colorPicker = colorPickers[i];
    colorPicker.onclick = changeColor;
}

$("#steelblue").click();