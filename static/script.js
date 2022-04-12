var positions = ['tight', 'none', 'move-left', 'move-right'];

function hand_change(hand_pattern) {
  for (var i = 1; i < (hand_pattern.length + 1); i++) {
    var hand = document.getElementById('f_'+ i);
    for (var x = 0; x < positions.length; x++) {
      hand.classList.remove(positions[x]);
    }
    hand.classList.add(hand_pattern[i-1]);
  }
}

function hand_gun() {
  var hand = ['tight', 'none', 'none', 'tight', 'tight'];
  hand_change(hand);
}

function hand_metal() {
  var hand = ['tight', 'none', 'tight', 'tight', 'none'];
  hand_change(hand);
}

function hand_pointer() {
  var hand = ['tight', 'none', 'tight', 'tight', 'tight'];
  hand_change(hand);
}

function menjimpit() {
  var hand = ['tight', 'tight', 'tight', 'none', 'none'];
  hand_change(hand);
}
function menggengam() {
  var hand = ['tight', 'tight', 'tight', 'tight', 'tight'];
  hand_change(hand);
}

function santai() {
  var hand = ['none', 'none', 'none', 'none', 'none'];
  hand_change(hand);
}

function hand_rock() {
  var hand = ['tight', 'tight', 'tight', 'tight', 'tight'];
  hand_change(hand);
}

function hand_middle() {
  var hand = ['tight', 'tight', 'none', 'tight', 'tight'];
  hand_change(hand);
}

function hand_scissor() {
  var hand = ['tight', 'move-left', 'move-right', 'tight', 'tight'];
  hand_change(hand);
}

function hand_spock() {
  var hand = ['none', 'move-left', 'move-left', 'move-right', 'move-right'];
  hand_change(hand);
}

function hand_cross() {
  var hand = ['tight', 'move-right', 'move-left', 'tight', 'tight'];
  hand_change(hand);
}

function hand_paper() {
  var hand = ['none', 'none', 'none', 'none', 'none'];
  hand_change(hand);
}

function hand_custom() {
  var hand = [document.getElementById('select_f1').value, 
              document.getElementById('select_f2').value, 
              document.getElementById('select_f3').value, 
              document.getElementById('select_f4').value, 
              document.getElementById('select_f5').value];
  hand_change(hand);
}


const source = new EventSource("data");


source.onmessage = function (event) {
    const data = JSON.parse(event.data);
    console.log (data.value)
    if (data.value ==0){
      santai()
    }
    else if (data.value ==1){
      menggengam()
    }
    else if (data.value ==2){
      menjimpit()

    
    }

}