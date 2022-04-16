var top_4 = document.getElementById("trophy_btn");
var modal_top_4 = document.getElementById('top_modat4')
top_4.addEventListener('click', () => {
    modal_top_4.style.display = "block"
    $('#data').empty()
    $.ajax({
        url: domain + '/api/top10',
        success: (data) => {
            let str = ''
            data['data'].forEach((el, index) => {
                if (index == 0 && el['score'] > 0) {
                    let item =
                        `
                    <div class="row">
                    <div class="col">${index+1} </div>
                    <div class="col">${el['nickname']}</div>
                    <div class="col">${el['score']}</div>
                    <div class="col">&#11088 &#11088 &#11088</div>
                    </div>
                    `
                    str += item

                } else if (index == 1 && el['score'] > 0) {
                    let item =
                        `
                    <div class="row">
                    <div class="col">${index+1}</div>
                    <div class="col">${el['nickname']}  </div>
                    <div class="col">${el['score']}</div>
                    <div class="col">&#11088&#11088</div>
                    </div>
                    `
                    str += item

                } else if (index == 2 && el['score'] > 0) {
                    let item =
                        `
                    <div class="row">
                    <div class="col">${index+1}</div>
                    <div class="col">${el['nickname']} </div>
                    <div class="col">${el['score']}</div>
                    <div class="col">&#11088</div>
                    </div>
                    `
                    str += item

                } else {
                    let item =
                        `
                    <div class="row">
                    <div class="col">${index+1}</div>
                    <div class="col">${el['nickname']}</div>
                    <div class="col">${el['score']}</div>
                    </div>
                    `
                    str += item

                }


            });
            $('#data').append(str)


        },
        error: (err) => {
            console.log(err);
        }

    })
})
var span_4 = document.querySelector('.close_top')
span_4.onclick = function() {
    modal_top_4.style.display = "none";
}