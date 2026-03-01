function removeComments(instr, remblanks) {
  let builder=[];
  let lines = instr.split("\n");
  for (let i = 0; i < (lines.length - 1); i++) {
    let line = lines[i];
    if (line.trimStart().indexOf("#") != 0) {
      if (((remblanks === true) && (line.trimStart().length >= 1)) || (remblanks === false)) {
        builder.push(line);
      }
    }
  }
  return builder.join("\n");
}

function getComments(instr) {
  let builder=[];
  let lines = instr.split("\n");
  for (let i = 0; i < (lines.length - 1); i++) {
    let line = lines[i];
    if ((line.trimStart().indexOf("#") == 0) && (line.trimStart().length >= 1)) {
      builder.push(line);
    }
  }
  return builder.join("\n");
}

function cheapFixTeleporters(instr) {
  let builder=[];
  let lines = instr.split("\n");
  let tele=0;
  for (let i = 0; i < (lines.length - 1); i++) {
    let line = lines[i].trimStart();
    if ((line.indexOf("#") != 0) && (line.length >= 1)) {
      if (tele === 1) { if(line.indexOf("name") == 0) {tele=0; continue;} }
      else {if (line.indexOf("teleporter") == 0) {tele=1;}}
      builder.push(line);
    }
  }
  return builder.join("\n");
}

