const hangulMap = {
    q: 'ㅂ',
    w: 'ㅈ',
    e: 'ㄷ',
    r: 'ㄱ',
    t: 'ㅅ',
    y: 'ㅛ',
    u: 'ㅕ',
    i: 'ㅑ',
    o: 'ㅐ',
    p: 'ㅔ',
    a: 'ㅁ',
    s: 'ㄴ',
    d: 'ㅇ',
    f: 'ㄹ',
    g: 'ㅎ',
    h: 'ㅗ',
    j: 'ㅓ',
    k: 'ㅏ',
    l: 'ㅣ',
    z: 'ㅋ',
    x: 'ㅌ',
    c: 'ㅊ',
    v: 'ㅍ',
    b: 'ㅠ',
    n: 'ㅜ',
    m: 'ㅡ',
  };
  
  document.getElementById('input').addEventListener('input', function() {
    const inputText = this.value;
    let outputText = '';
    
    for (let i = 0; i < inputText.length; i++) {
      const char = inputText[i].toLowerCase();
      outputText += hangulMap[char] || inputText[i];
    }
    
    this.value = outputText;
  });