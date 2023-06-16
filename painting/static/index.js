document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('videoIntroduce').addEventListener('ended', function(){
        closeModal();
    })
})
function closeModal(){
    var modal = document.getElementById("introduce");
    modal.style.display = "none";
}