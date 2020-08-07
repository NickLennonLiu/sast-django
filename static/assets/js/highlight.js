const paras = document.querySelectorAll(".matched");

function highlight() {
    const keyword = document.querySelector("input").placeholder;
    const replacement = "<span class='highlight'>" + keyword + "</span>";
    for (let i = 0;i<=paras.length;i++){
        const para = paras[i];
        let str = para.innerHTML;
        str = str.split(keyword).join(replacement);
        para.innerHTML = str;
    }
}

highlight()
/*
<script>
    $(() => {
      const texts = $('main p, main a');
      const keyword = "123";
      for (let i = 0; i < texts.length; i++) {
          const text = texts[i];
          let str = text.innerHTML;
          if (str.indexOf(keyword) != -1) {
            str = str.split(keyword).join("<span class='highlight'>" + keyword + "</span>");
            text.innerHTML = str;
          }
      }
    });
</script>

 */