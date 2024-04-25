const cyrillicMap = {
    a: 'а',
    b: 'б',
    c: 'ц',
    d: 'д',
    e: 'е',
    f: 'ф',
    g: 'г',
    h: 'х',
    i: 'и',
    j: 'й',
    k: 'к',
    l: 'л',
    m: 'м',
    n: 'н',
    o: 'о',
    p: 'п',
    q: 'я',
    r: 'р',
    s: 'с',
    t: 'т',
    u: 'у',
    v: 'в',
    w: 'ш',
    x: 'ж',
    y: 'ы',
    z: 'з',
  };
  
  document.getElementById('input').addEventListener('input', function() {
    const inputText = this.value;
    let outputText = '';
    
    for (let i = 0; i < inputText.length; i++) {
      const char = inputText[i].toLowerCase();
      outputText += cyrillicMap[char] || inputText[i];
    }
    
    this.value = outputText;
  });