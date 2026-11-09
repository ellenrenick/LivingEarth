  /* ---------- hands-on reteach engine ---------- */
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function pickOne(a) { return a[Math.floor(Math.random() * a.length)]; }
  function kids(node, fn) { Array.prototype.forEach.call(node.children, fn); }
  function chips(arr) { return arr.map(function (x) { return '<span class="chip">' + esc(x) + "</span>"; }).join(""); }
  function geno(x, y) { return (x === x.toLowerCase() && y !== y.toLowerCase()) ? y + x : x + y; }

  function mountReteach(it) {
    var host = document.getElementById("react"), r = it.reteach || {}, queue = [];
    host.innerHTML = '<h3 class="rhead">Not quite. Let’s work it out.</h3>';
    if (r.sort) queue.push(function (n) { runSort(host, r.sort, n); });
    if (r.viz) queue.push(function (n) { runViz(host, r.viz, n); });
    if (r.steps) queue.push(function (n) { runSteps(host, r.steps, n); });
    function go(i) { if (i >= queue.length) return finish(); queue[i](function () { go(i + 1); }); }
    function finish() {
      var why = S.sel.filter(function (ci) { return !it.choices[ci].ok && it.choices[ci].why; }).map(function (ci) { return it.choices[ci].why; });
      var d = el("div", "rdone", '<p class="keyidea">' + esc(it.key) + "</p>" + (why.length ? "<p>About the answer you picked: " + esc(why[0]) + "</p>" : "") + '<div class="row"><button type="button" id="rt2">Try the question again</button></div>');
      host.appendChild(d);
      document.getElementById("rt2").addEventListener("click", retry);
      d.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
    go(0);
  }

  /* guided steps: o[0] is the right option; options are shuffled on screen */
  function runSteps(host, steps, done) {
    var box = el("div", "steps"); host.appendChild(box);
    function show(i) {
      if (i >= steps.length) return done();
      var st = steps[i], d = el("div", "step"), opts = el("div", "stepopts"), fb = el("p", "stepfb");
      fb.setAttribute("aria-live", "polite");
      d.appendChild(el("p", "stepq", "<b>" + (i + 1) + ".</b> " + esc(st.q)));
      shuffle(st.o.map(function (_, k) { return k; })).forEach(function (k) {
        var b = el("button", "opt"); b.type = "button"; b.textContent = st.o[k];
        b.addEventListener("click", function () {
          if (k === 0) {
            kids(opts, function (x) { x.disabled = true; });
            b.classList.add("ok"); fb.className = "stepfb good"; fb.textContent = st.right || "Yes.";
            show(i + 1);
          } else {
            b.classList.add("x"); b.disabled = true; fb.className = "stepfb bad";
            fb.textContent = (st.hints && st.hints[k]) || "Not quite. Try another.";
          }
        });
        opts.appendChild(b);
      });
      d.appendChild(opts); d.appendChild(fb); box.appendChild(d);
    }
    show(0);
  }

  /* sort: each card goes into one of two buckets, with feedback on every card */
  function runSort(host, cfg, done) {
    var box = el("div", "sortbox"), left = cfg.cards.length; host.appendChild(box);
    box.appendChild(el("p", "stepq", esc(cfg.prompt)));
    shuffle(cfg.cards).forEach(function (c) {
      var row = el("div", "sortrow"), btns = el("div", "sortbtns"), fb = el("p", "stepfb");
      fb.setAttribute("aria-live", "polite");
      cfg.buckets.forEach(function (name, bi) {
        var b = el("button", "opt"); b.type = "button"; b.textContent = name;
        b.addEventListener("click", function () {
          if (bi === c.b) {
            kids(btns, function (x) { x.disabled = true; });
            b.classList.add("ok"); fb.className = "stepfb good"; fb.textContent = c.why;
            left--; if (left === 0) done();
          } else { b.classList.add("x"); b.disabled = true; fb.className = "stepfb bad"; fb.textContent = "Not that one. Try the other."; }
        });
        btns.appendChild(b);
      });
      row.appendChild(el("p", "sorttext", "<b>" + esc(c.t) + "</b>")); row.appendChild(btns); row.appendChild(fb); box.appendChild(row);
    });
  }

  function runViz(host, cfg, done) {
    var box = el("div", "viz"); host.appendChild(box);
    VIZ[cfg.type](box, cfg, done);
  }
  var VIZ = {};

  /* make sex cells from a body cell: each gets one allele */
  VIZ.sexcells = function (box, cfg, done) {
    var a = cfg.alleles, n = 0, fired = false, tally = {};
    a.forEach(function (x) { tally[x] = 0; });
    box.innerHTML = '<p class="stepq">' + esc(cfg.prompt) + '</p><div class="cellrow"><span class="lab">Body cell</span>' + chips(a) + '</div>' +
      '<div class="row"><button type="button" class="mk">Make a sex cell</button><span class="status vc"></span></div>' +
      '<div class="cellrow vo"><span class="lab">Sex cells</span></div><p class="status vt"></p>';
    var out = box.querySelector(".vo"), vc = box.querySelector(".vc"), vt = box.querySelector(".vt");
    box.querySelector(".mk").addEventListener("click", function () {
      var x = pickOne(a); n++; tally[x]++;
      out.appendChild(el("span", "chip sc", esc(x)));
      vt.textContent = a.map(function (y) { return y + ": " + tally[y]; }).join("   ");
      if (n < 4) vc.textContent = n + " of 4"; else if (!fired) { fired = true; vc.textContent = "Good. Keep going, or answer the questions below."; done(); }
    });
  };

  /* join one sex cell from each parent */
  VIZ.fertilize = function (box, cfg, done) {
    var n = 0, fired = false, seen = [];
    box.innerHTML = '<p class="stepq">' + esc(cfg.prompt) + '</p><div class="cellrow"><span class="lab">Mom</span>' + chips(cfg.p1) + '<span class="lab spc">Dad</span>' + chips(cfg.p2) + '</div>' +
      '<div class="row"><button type="button" class="mk">Make a ' + esc(cfg.who) + '</button><span class="status vc"></span></div>' +
      '<div class="listbox vo"></div><p class="status vt"></p>';
    var out = box.querySelector(".vo"), vc = box.querySelector(".vc"), vt = box.querySelector(".vt");
    box.querySelector(".mk").addEventListener("click", function () {
      n++;
      var fx = cfg.fixed && cfg.fixed[n], e = fx ? fx[0] : pickOne(cfg.p1), s = fx ? fx[1] : pickOne(cfg.p2);
      [e, s].forEach(function (x) { if (seen.indexOf(x) < 0) seen.push(x); });
      out.appendChild(el("div", "chrow", "<span>egg</span>" + chips([e]) + "<span>+ sperm</span>" + chips([s]) + "<span>→ " + esc(cfg.who) + "</span><b class=\"geno\">" + esc(geno(e, s)) + "</b>"));
      vt.textContent = "Alleles in the " + (cfg.plural || cfg.who + "s") + " so far: " + seen.join(", ");
      if (n < 4) vc.textContent = n + " of 4"; else if (!fired) { fired = true; vc.textContent = "Good. Keep going, or answer the questions below."; done(); }
    });
  };

  /* crossing over: swap the bottom pieces of paired chromosomes */
  VIZ.crossover = function (box, cfg, done) {
    var c1 = [{ l: "A", o: 1 }, { l: "B", o: 1 }, { l: "C", o: 1 }], c2 = [{ l: "a", o: 2 }, { l: "b", o: 2 }, { l: "c", o: 2 }], fired = false;
    box.innerHTML = '<p class="stepq">' + esc(cfg.prompt) + '</p><div class="chroms"><div class="chrom c1"></div><div class="chrom c2"></div></div>' +
      '<div class="row"><button type="button" class="mk">Cross over</button><button type="button" class="opt rs" hidden>Reset</button></div><p class="status vt"></p>';
    var vt = box.querySelector(".vt"), rs = box.querySelector(".rs");
    function draw() {
      [c1, c2].forEach(function (c, k) {
        box.querySelector(".c" + (k + 1)).innerHTML = c.map(function (s) { return '<div class="seg s' + s.o + '">' + esc(s.l) + "</div>"; }).join("");
      });
    }
    function swap() { var t = c1[2]; c1[2] = c2[2]; c2[2] = t; draw(); }
    draw();
    box.querySelector(".mk").addEventListener("click", function () {
      swap(); rs.hidden = false;
      vt.textContent = "Same pieces, new mix: " + c1.map(function (s) { return s.l; }).join(" ") + " and " + c2.map(function (s) { return s.l; }).join(" ") + ".";
      if (!fired) { fired = true; done(); }
    });
    rs.addEventListener("click", function () { c1 = [{ l: "A", o: 1 }, { l: "B", o: 1 }, { l: "C", o: 1 }]; c2 = [{ l: "a", o: 2 }, { l: "b", o: 2 }, { l: "c", o: 2 }]; draw(); vt.textContent = ""; });
  };

  /* spot the copying error */
  VIZ.spot = function (box, cfg, done) {
    box.innerHTML = '<p class="stepq">' + esc(cfg.prompt) + '</p><div class="cellrow"><span class="lab">Original</span>' + chips(cfg.orig.split("")) + '</div>' +
      '<div class="cellrow cp"><span class="lab">Copy</span></div><p class="stepfb vt" aria-live="polite"></p>';
    var cp = box.querySelector(".cp"), vt = box.querySelector(".vt");
    cfg.copy.split("").forEach(function (ch, i) {
      var b = el("button", "chip btn", esc(ch)); b.type = "button";
      b.addEventListener("click", function () {
        if (ch !== cfg.orig[i]) { b.classList.add("ok"); vt.className = "stepfb good vt"; vt.textContent = cfg.found; kids(cp, function (x) { x.disabled = true; }); done(); }
        else { b.classList.add("x"); b.disabled = true; vt.className = "stepfb bad vt"; vt.textContent = "That letter matches the original. Look for the one that is different."; }
      });
      cp.appendChild(b);
    });
  };

  /* change one DNA letter and watch the amino acid change */
  VIZ.codon = function (box, cfg, done) {
    box.innerHTML = '<p class="stepq">' + esc(cfg.prompt) + '</p><div class="cellrow"><span class="lab">DNA</span><span class="dna">' + chips(cfg.before.split("")) + '</span></div>' +
      '<p class="stepq">Amino acid: <b class="aa">' + esc(cfg.aa1) + '</b></p><div class="row"><button type="button" class="mk">Change one letter</button></div>';
    var btn = box.querySelector(".mk");
    btn.addEventListener("click", function () {
      box.querySelector(".dna").innerHTML = chips(cfg.after.split(""));
      box.querySelector(".aa").textContent = cfg.aa2; btn.disabled = true; done();
    });
  };

  /* tap the boxes of a Punnett square that match a genotype */
  VIZ.punnett = function (box, cfg, done) {
    var total = 0, found = 0;
    cfg.grid.forEach(function (r, ri) { r.forEach(function (c, ci) { if (ri > 0 && ci > 0 && c === cfg.target) total++; }); });
    box.innerHTML = '<p class="stepq">' + esc(cfg.prompt) + '</p><div class="scroll"><table class="punnett pk"></table></div><p class="stepfb vt" aria-live="polite"></p>';
    var tb = box.querySelector(".pk"), vt = box.querySelector(".vt");
    cfg.grid.forEach(function (r, ri) {
      var tr = el("tr");
      r.forEach(function (c, ci) {
        if (ri === 0 || ci === 0) { tr.appendChild(el("th", "", esc(c))); return; }
        var td = el("td", "pcell", esc(c)); td.tabIndex = 0; td.setAttribute("role", "button");
        function tap() {
          if (td.className.indexOf("ok") >= 0) return;
          if (c === cfg.target) { td.classList.add("ok"); found++; vt.className = "stepfb good vt"; vt.textContent = found === total ? cfg.found : "Yes. Keep looking."; if (found === total) done(); }
          else { td.classList.add("x"); vt.className = "stepfb bad vt"; vt.textContent = "That box is " + c + ". Look for " + cfg.target + "."; }
        }
        td.addEventListener("click", tap);
        td.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); tap(); } });
        tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  };

