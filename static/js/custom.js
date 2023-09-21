function sendArticleComment(articleId){
    var comment = $('#commentText').val()

    // ajx => asynchronous javascript and xml

    $.get('/articles/add-article-comment', {
        articleComment: comment,
        articleId : articleId,
        parentId: null
    }).then(res => {

    });
}