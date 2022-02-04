//!Search Field Cars

console.log('Hello World from home.html')

let sliderneyse = document.getElementsByClassName('ui-slider-handle ui-state-default ui-corner-all')[0]

//console.log(sliderneyse);


//!SearchInputValueByCar
// let carName = document.getElementById('car_name')

//!SelectedModel
// function selectModel(){
//     let select_model = document.getElementById('select_model')
//     let selectModelText = select_model.options[select_model.selectedIndex].text//yeni optionslar icinde secilen indexin text deyerini aldig
//     return selectModelText
// }

//Ve Ya
let selectedModelText = ''
document.getElementById('select_model').addEventListener('change',(e)=>{
    e.preventDefault()
    selectedModelText = e.target.value
})

//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


//!SelectedLocation
// function selectLocation(){
//     let select_location = document.getElementById('select_location')
//     let selectLocationText = select_location.options[select_location.selectedIndex].text
//     console.log(selectLocationText)
// }

//Ve Ya
let selectedLocationText = ''
document.getElementById('select_location').addEventListener('change',(e)=>{
    e.preventDefault()
    selectedLocationText = e.target.value
})
//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

//!SelectedYear
// function selectedYear(){
//     let select_year = document.getElementById('select_year')
//     let selectLocationText = select_year.options[select_year.selectedIndex].text
//     console.log(selectLocationText)
// }

//Ve Ya
let selectYearText = ''
document.getElementById('select_year').addEventListener('change',(e)=>{
    e.preventDefault()
    selectYearText = e.target.value
})
//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

//!SelectedBodyStyle
// function selectBodyStyle(){
//     let select_body_style = document.getElementById('select_body_style')
//     let selectBodyStyleText = select_body_style.options[select_body_style.selectedIndex].text
//     console.log(selectBodyStyleText)
// }

let selectBodyStyleText = ''
document.getElementById('select_body_style').addEventListener('change',(e)=>{
    e.preventDefault()
    selectBodyStyleText = e.target.value
})

//!SelectPriceCarMax
let selectedPriceTextMax = ''
function selectPriceCarMax(){
    //let select_car_price_max = document.getElementById('select_price').getAttribute('data-min-name').value
    let select_car_price_max = document.getElementsByClassName('max-value')

    for(let i=0;i<select_car_price_max.length;i++){
        //console.log(select_car_price_max[i].textContent.trim())
        selectedPriceTextMax = select_car_price_max[i].textContent.replace('USD','').trim()
        console.log(`Secilen Maksimum Deyer : ${Number(selectedPriceTextMax)}`);
        // console.log(typeof(selectedPriceTextMax))
    }
}
let select_car_price_max = document.getElementById('select_price')
select_car_price_max.addEventListener('mouseup',selectPriceCarMax)//mouseup => olanda mouseu basib buraxanda isleyir,mouse downda ise tersine buraxib yeniden basanda isleyir ele bil

//!SelectedPriceCarMin
let selectedPriceTextMin = ''
var resultCarPrice = 0
function selectPriceCarMin(){
    let select_car_price_min = document.getElementsByClassName('min-value')
    
    for(let i=0;i<select_car_price_min.length;i++){
        selectedPriceTextMin = select_car_price_min[i].textContent.replace('USD','').trim()
        console.log(`Minimum Secilen Deyer ${Number(selectedPriceTextMin)}`)
        // console.log(typeof(selectedPriceTextMin))
        // resultCarPrice =  selectedPriceTextMax-selectedPriceTextMin
        // console.log('Yekun Mebleg ' + resultCarPrice);
    }
}
let select_car_price_min = document.getElementById('select_price')
select_car_price_min.addEventListener('mouseup',selectPriceCarMin)

//!selectecIndex => sayesinde dropdownlarda secilen rowun indexini geri dondere bilirik => selectedIndex sayesinde yeni --- secilenIndex
//!options => sayesinden ise dropdowndaki butun elementleri secmek mumkundur yeni elde etmek menasinda => options sayesinde yeni --- secimler

//const search_form = document.getElementById('search_form')
//const select_model = document.getElementById('select-model')
//let dspValue = select_model.options[select_model.selectedIndex].value => value ve ya text coxda ferq elemir


//!Ajax csrftoken
const getCookie = (name) => {//js de funksiyalari deyisken kimi tanimlamag mumkundur
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


//!Search Form Car
const formSearch = document.getElementById('search_form')
const currently_url = window.location.href+"cars/getdatacar"
const car_list_search_result = document.getElementById('car_list_search_result')

formSearch.addEventListener('submit',(e)=>{
    e.preventDefault()
    console.log('Form Submit Oldu Masin Axtarisi Ucun Olan Form...')

    car_list_search_result.innerHTML = ''

    if(selectedModelText=='' || selectedLocationText=='' || selectYearText=='' || selectBodyStyleText == ''){
        alert('Input True Value Please')
        location.href = window.location.href
    }
    

    const gorunmez = document.getElementById('gorunmez')
    gorunmez.innerHTML = '<div class="page_loader"></div>'
    setTimeout(()=>{
        gorunmez.innerHTML = ''
    },1500)

    $.ajax({
        type:'POST',
        url:currently_url,
        data:{
            'csrfmiddlewaretoken':csrftoken,
            //'CarName':carName.value,
            'Model':selectedModelText,
            'Location':selectedLocationText,
            'Year':selectYearText,
            'BodyStyle':selectBodyStyleText,
            'CarPriceMax':selectedPriceTextMax,
            'CarPriceMin':selectedPriceTextMin, 
        },
        success:function(response){
            //console.log(response)
            const cars_list = [...JSON.parse(response.cars_list)]
            //location.href = 'http://127.0.0.1:8000/cars/search'
            formSearch.reset()//reset funksiyasi sayesinde atilan requestden sonra form icinde butun deyerler temizlene bilir
            selectedModelText = ''
            selectedLocationText = ''
            selectYearText = ''
            selectBodyStyleText = ''
            //buralari sifirlamasan yuxarida atadigin deyerler qalacag icinde

            cars_list.forEach(function(car){
                let result_car_fields = car.fields

                let car_detail_url = window.location.href+`cars/${car.pk}`

                console.log(car_detail_url);    

                //yeni ana page html ve body dir scroolTop ile animate ile endirirem lazim olan qeder asagi return false et mutleq
                $('html,body').animate({scrollTop:1800},200)


                let result_picture = window.location.href+`media/${result_car_fields.car_photo}`

                car_list_search_result.innerHTML += `
                        <div class="col-lg-4 col-md-6">
                        <div class="car-box">
                            <div class="car-thumbnail">
                                <a href=${car_detail_url} class="car-img">
                                    <div class="tag">For Sale</div>
                                    <img class="d-block w-100" src=${result_picture} style="min-height: 262px !important;max-height: 262px !important;" alt="car">
                                    <div class="facilities-list clearfix">
                                        <ul>
                                            <li>
                                                <span><i class="flaticon-way"></i></span>${result_car_fields.miles} km
                                            </li>
                                            <li>
                                                <span><i class="flaticon-calendar-1"></i></span>${result_car_fields.year}
                                            </li>
                                            <li>
                                                <span><i class="flaticon-manual-transmission"></i></span>${result_car_fields.transmission}
                                            </li>
                                        </ul>
                                    </div>
                                </a>
                            </div>
                            <div class="detail">
                                <h1 class="title">
                                    <a href="${car_detail_url}">${result_car_fields.car_title}</a>
                                </h1>
                                <div class="location">
                                    <a href="${car_detail_url}">
                                        <i class="flaticon-pin"></i>${result_car_fields.state}. ${result_car_fields.city}
                                    </a>
                                </div>
                            </div>
                            <div class="footer clearfix">
                                <div class="pull-left ratings days">
                                    <p class="cartype">${result_car_fields.body_style}</p>
                                </div>
                                <div class="pull-right">
                                    <p class="price">${result_car_fields.price}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `
            })
            

            console.log(window.location.href)//!href duzeltmek lazimdir
        },
        error:function(err){
            console.log(err)
        }
    })

    // console.log('CarName ', carName.value)
    // console.log('Model ', selectedModelText)
    // console.log('Location ', selectedLocationText)
    // console.log('Year', selectYearText)
    // console.log('Body Style', selectBodyStyleText)
    // console.log('Car Price ', selectedPriceText)


})
