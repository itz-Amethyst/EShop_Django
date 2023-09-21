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