
function BZRandom(input, groupname) {
  let buffer=[];
  let iput = parseInt(input);
  for(let i = 0; i < iput; i++) {
    let rand1  = Math.floor(Math.random() * (400 + 1));
    let rand2  = Math.floor(Math.random() * (400 + 1));
    let rand3  = (Math.random() * 2);
    buffer.push("");
    // x y
    buffer.push("group ".concat(groupname, "\nname ", i));
    buffer.push("position ".concat(rand1, " ", rand2, " 0"));
    buffer.push("size ".concat(rand3.toFixed(3), " ", rand3.toFixed(3), " ", rand3.toFixed(3), "\nend"));
    // -x -y
    buffer.push("group ".concat(groupname, "\nname ", i));
    buffer.push("position ".concat(rand1 * -1, " ", rand2 * -1, " 0"));
    buffer.push("size ".concat(rand3.toFixed(3), " ", rand3.toFixed(3), " ", rand3.toFixed(3), "\nend"));
    // -x y
    buffer.push("group ".concat(groupname, "\nname ", i));
    buffer.push("position ".concat(rand1 * -1, " ", rand2, " 0"));
    buffer.push("size ".concat(rand3.toFixed(3), " ", rand3.toFixed(3), " ", rand3.toFixed(3), "\nend"));
    // x -y
    buffer.push("group ".concat(groupname, "\nname ", i));
    buffer.push("position ".concat(rand1, " ", rand2 * -1, " 0"));
    buffer.push("size ".concat(rand3.toFixed(3), " ", rand3.toFixed(3), " ", rand3.toFixed(3), "\nend"));
  }
  return buffer.join("\n");
}
