(($, document, window) => {
    $('.cp-spinner').hide()
    const getNowFormatDate = () => {
        let date = new Date();
        let seperator1 = "-";
        let seperator2 = ":";
        let month = date.getMonth() + 1;
        let strDate = date.getDate();
        if (month >= 1 && month <= 9) {
            month = "0" + month;
        }
        if (strDate >= 0 && strDate <= 9) {
            strDate = "0" + strDate;
        }
        let currentdate = date.getYear() + seperator1 + month + seperator1 + strDate
            + " " + date.getHours() + seperator2 + date.getMinutes()
            + seperator2 + date.getSeconds();
        return currentdate;
    }
    $('textarea').each(function () {
        this.setAttribute('style', 'height:' + (this.scrollHeight) + 'px;overflow-y:hidden;');
      }).on('input', function () {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
      });
    $('.download').click(async () => {
        try {
            $('.cp-spinner').show()
            $('.download').prop("disabled", true);
            const sentence = $('#floatingTextarea').val()
            const requstData = {
                'sentence': sentence,
                'lang': 'zh-tw'
            }
            const req = await fetch('/upload-text', {
                method: 'POST', // or 'PUT'
                body: JSON.stringify(requstData),
                headers: new Headers({
                    'Content-Type': 'application/json'
                })
            })
            const res = await req.blob()
            const url = window.URL.createObjectURL(res);
            var a = document.createElement('a');
            a.href = url;
            a.download = `${getNowFormatDate()}.mp3`;
            document.body.appendChild(a);
            a.click();
            a.remove();
        } catch (error) {
            alert(error)
        }
        finally {
            $('.cp-spinner').hide()
            $('.download').prop("disabled", false);
        }


    })
})($, document, window)