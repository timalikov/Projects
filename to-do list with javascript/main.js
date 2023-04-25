//
//ADD LIST ITEMS
//

//variables
alert("Check if connected")

// const addInput = document.getElementById("#addInput");
const addBtn = document.querySelector("#addBtn");
let listGroup = document.querySelector('.list-group');


addBtn.addEventListener('click', AddTask)

function AddTask(){
    let taskName = document.getElementById('addInput').value;
    
    let taskDetails = `<label class="list-group-item" id="myText">
            <input class="form-check-input me-1" type="checkbox" value="" id="myCheckbox">
            ${taskName}
            <button class="delete-button float-end" onclick="deleteCheckbox(event)"><i class="fas fa-trash"></i></button>
        </label>`;
    if(taskName){
        listGroup.insertAdjacentHTML('beforeend', taskDetails);
    }else{
        console.log("Task is empty");
    }
    
}



//
//CROSS-OUT WHEN CLICK
//
let checkbox = document.querySelectorAll('input[type=checkbox]');
let text = document.querySelectorAll('#myText');

// checkbox.addEventListener('click', function() {
//     if (this.checked) {
//       text.classList.add('strikethrough');
//     } else {
//       text.classList.remove('strikethrough');
//     }
//   });
for (let i = 0; i < checkbox.length; i++) {
    checkbox[i].addEventListener('click', function() {
      if (this.checked) {
        text[i].classList.add('strikethrough');
      } else {
        text[i].classList.remove('strikethrough');
      }
    });
  }


//
//DELETE ITEMS
//
let deleteBtn = querySelectorAll('#delete');

function deleteCheckbox(event) {
    const checkbox = event.target.previousElementSibling.previousElementSibling;
    const div = event.target.parentNode;
    div.parentNode.removeChild(div);
  }

  
// for(let i = 0; i < deleteBtn.length; i++){
//     deleteBtn[i].addEventListener('clcik', function(){
        
//     })
// }






















//     // console.log("Clicked")
//     let lavel = document.createElement('label');
//     lavel.classList.add('list-group-item');
//     let inp = document.createElement('INPUT');
//     inp.classList.add('form-check-input');
//     inp.classList.add('me-1');
//     inp.type == "checkbox";
//     // listGroup.appendChild(lavel, inp);
//     listGroup.appendChild(lavel);
//     listGroup.appendChild(inp);

//     // listGroup.append('<input type="checkbox" class="form-check-input me-1" />' + $(".txt").val());
// })

// $(document).ready(function () {
//     $("#addBtn").on('click', function () {
//         $('#check').append('<input type="checkbox" class="form-check-input me-1"/>' + $("#addInput").val());
//     });
// });


