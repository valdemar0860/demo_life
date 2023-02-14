// drag
const items = document.querySelectorAll("[draggable=true]");

for (const item of items) {
  item.addEventListener("dragstart", handleDragStart);
  item.addEventListener("drag", handleDrag);
  item.addEventListener("dragend", handleDragEnd);
}

function handleDragStart(e) {
  e.dataTransfer.setData("text", e.target.id);
}

function handleDrag(e) {
  // This event is optional and not necessary for this example
}

function handleDragEnd(e) {
  const data = e.dataTransfer.getData("text");
  e.target.style.display = "none";
  const target = document.getElementById(data);
  target.style.display = "block";
}

// drop
const target = document.getElementById("target");

target.addEventListener("dragover", handleDragOver);
target.addEventListener("drop", handleDrop);

function handleDragOver(e) {
  e.preventDefault();
}

function handleDrop(e) {
  e.preventDefault();
  const data = e.dataTransfer.getData("text");
  const target = document.getElementById(data);
  e.target.appendChild(target);
}
