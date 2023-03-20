var app=function(){"use strict";function t(){}function e(t){return t()}function n(){return Object.create(null)}function o(t){t.forEach(e)}function r(t){return"function"==typeof t}function c(t,e){return t!=t?e==e:t!==e||t&&"object"==typeof t||"function"==typeof t}function u(t,e){t.appendChild(e)}function a(t){t.parentNode&&t.parentNode.removeChild(t)}function s(t){return document.createElement(t)}function i(t){return document.createTextNode(t)}function f(t,e,n){null==n?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}let l;function d(t){l=t}const p=[],h=[];let $=[];const m=[],g=Promise.resolve();let y=!1;function b(t){$.push(t)}const _=new Set;let x=0;function v(){if(0!==x)return;const t=l;do{try{for(;x<p.length;){const t=p[x];x++,d(t),k(t.$$)}}catch(t){throw p.length=0,x=0,t}for(d(null),p.length=0,x=0;h.length;)h.pop()();for(let t=0;t<$.length;t+=1){const e=$[t];_.has(e)||(_.add(e),e())}$.length=0}while(p.length);for(;m.length;)m.pop()();y=!1,_.clear(),d(t)}function k(t){if(null!==t.fragment){t.update(),o(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(b)}}const E=new Set;function w(t,e){const n=t.$$;null!==n.fragment&&(!function(t){const e=[],n=[];$.forEach((o=>-1===t.indexOf(o)?e.push(o):n.push(o))),n.forEach((t=>t())),$=e}(n.after_update),o(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function j(t,e){-1===t.$$.dirty[0]&&(p.push(t),y||(y=!0,g.then(v)),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function N(c,u,s,i,f,p,h,$=[-1]){const m=l;d(c);const g=c.$$={fragment:null,ctx:[],props:p,update:t,not_equal:f,bound:n(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(u.context||(m?m.$$.context:[])),callbacks:n(),dirty:$,skip_bound:!1,root:u.target||m.$$.root};h&&h(g.root);let y=!1;if(g.ctx=s?s(c,u.props||{},((t,e,...n)=>{const o=n.length?n[0]:e;return g.ctx&&f(g.ctx[t],g.ctx[t]=o)&&(!g.skip_bound&&g.bound[t]&&g.bound[t](o),y&&j(c,t)),e})):[],g.update(),y=!0,o(g.before_update),g.fragment=!!i&&i(g.ctx),u.target){if(u.hydrate){const t=function(t){return Array.from(t.childNodes)}(u.target);g.fragment&&g.fragment.l(t),t.forEach(a)}else g.fragment&&g.fragment.c();u.intro&&((_=c.$$.fragment)&&_.i&&(E.delete(_),_.i(x))),function(t,n,c,u){const{fragment:a,after_update:s}=t.$$;a&&a.m(n,c),u||b((()=>{const n=t.$$.on_mount.map(e).filter(r);t.$$.on_destroy?t.$$.on_destroy.push(...n):o(n),t.$$.on_mount=[]})),s.forEach(b)}(c,u.target,u.anchor,u.customElement),v()}var _,x;d(m)}class O{$destroy(){w(this,1),this.$destroy=t}$on(e,n){if(!r(n))return t;const o=this.$$.callbacks[e]||(this.$$.callbacks[e]=[]);return o.push(n),()=>{const t=o.indexOf(n);-1!==t&&o.splice(t,1)}}$set(t){var e;this.$$set&&(e=t,0!==Object.keys(e).length)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}function S(e){let n,o,r,c,l,d,p;return{c(){n=s("main"),o=s("h1"),r=i("Hello "),c=i(e[0]),l=i("!"),d=i(" "),p=s("p"),p.innerHTML='Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.',f(o,"class","svelte-1tky8bj"),f(n,"class","svelte-1tky8bj")},m(t,e){!function(t,e,n){t.insertBefore(e,n||null)}(t,n,e),u(n,o),u(o,r),u(o,c),u(o,l),u(n,d),u(n,p)},p(t,[e]){1&e&&function(t,e){e=""+e,t.wholeText!==e&&(t.data=e)}(c,t[0])},i:t,o:t,d(t){t&&a(n)}}}function A(t,e,n){let{name:o}=e;return t.$$set=t=>{"name"in t&&n(0,o=t.name)},[o]}return new class extends O{constructor(t){super(),N(this,t,A,S,c,{name:0})}}({target:document.getElementById("app-target"),props:JSON.parse(document.getElementById("app-props").textContent)})}();
//# sourceMappingURL=buildApp.js.map
