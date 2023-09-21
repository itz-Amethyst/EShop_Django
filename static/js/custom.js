function sendArticleComment(articleId){
    var comment = $('#commentText').val()
    var parentId = $('#parent_id').val()
    // ajx => asynchronous javascript and xml
    $.get('/articles/add-article-comment', {
        articleComment: comment,
        articleId : articleId,
        parentId: parentId
    }).then(res => {
        console.log(res)
        location.reload()
    });
}

function fillParentId(parentId) {
    debugger
    $('#parent_id').val(parentId)
    document.getElementById('comment_form_scroll').scrollIntoView({behavior:"smooth"})
}