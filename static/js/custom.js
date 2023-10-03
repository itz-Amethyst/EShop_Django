function sendArticleComment(articleId){
    var comment = $('#commentText').val()
    var parentId = $('#parent_id').val()
    // ajx => asynchronous javascript and xml
    $.get('/articles/add-article-comment', {
        articleComment: comment,
        articleId : articleId,
        parentId: parentId
    }).then(res => {
        $('#comment_response').html(res)
        $('#commentText').val('')
        $('#parent_id').val('')
        //! Note: Comment must be submitted by admin so these part is unusefull
        if(parentId !== null && parentId !== ''){
            document.getElementById('single_comment_box_' + parentId).scrollIntoView({behavior:"smooth"})
        }
        else{
            document.getElementById('comment_response').scrollIntoView({behavior:"smooth"})
        }
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId)
    document.getElementById('comment_form_scroll').scrollIntoView({behavior:"smooth"})
}

function FilterProducts(){
    const filterPrice = $('#sl2').val()
    const start_price = filterPrice.split(',')[0]
    const end_price = filterPrice.split(',')[1]

    $('#start_price').val(start_price)
    $('#end_price').val(end_price)

    $('#filter_form').submit()
}

function FillPage(page){
    $('#page').val(page)
    $('#filter_form').submit()
}

function ShowLargeImageProduct(imageSrc){
    $('#main_image').attr('src', imageSrc)
    $('#show_large_image_modal').attr('href', imageSrc)
}

function AddProductToOrder(productId){
    const productCount = $("#product_count").val()
    $.get('/order/add-to-order?product_id=' + productId + "&count=" + productCount).then(res=>{
        Swal.fire({
                title: "اعلان",
                text: res.text,
                icon: res.icon,
                confirmButtonText: res.confirm_button_text
            }).then(confirm =>{
                if (res.status === 'not_auth'){
                    window.location.href = '/login'
                }
        })
    })
}

function Remove_Item_In_OrderDetail(detailId){
    $.get('/user/remove-item-basket?detail_id=' + detailId).then(res =>{
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body)
        }
    })
}