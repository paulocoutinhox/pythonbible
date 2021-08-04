(self.webpackChunkpythonbible_docs=self.webpackChunkpythonbible_docs||[]).push([[7880],{3905:function(e,t,n){"use strict";n.d(t,{Zo:function(){return s},kt:function(){return m}});var r=n(7294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=r.createContext({}),p=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},s=function(e){var t=p(e.components);return r.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,o=e.mdxType,i=e.originalType,l=e.parentName,s=c(e,["components","mdxType","originalType","parentName"]),d=p(n),m=o,f=d["".concat(l,".").concat(m)]||d[m]||u[m]||i;return n?r.createElement(f,a(a({ref:t},s),{},{components:n})):r.createElement(f,a({ref:t},s))}));function m(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=n.length,a=new Array(i);a[0]=d;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c.mdxType="string"==typeof e?e:o,a[1]=c;for(var p=2;p<i;p++)a[p]=n[p];return r.createElement.apply(null,a)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},5948:function(e,t,n){"use strict";n.r(t),n.d(t,{frontMatter:function(){return a},metadata:function(){return c},toc:function(){return l},default:function(){return s}});var r=n(2122),o=n(9756),i=(n(7294),n(3905)),a={sidebar_position:8},c={unversionedId:"reference/count_chapters",id:"reference/count_chapters",isDocsHomePage:!1,title:"count_chapters",description:"The count_chapters function, given a string containing one or more Scripture references or a NormalizedReference object or a List of NormalizedReference objects, returns the int count of the chapters included in the given reference(s).",source:"@site/docs/reference/count_chapters.md",sourceDirName:"reference",slug:"/reference/count_chapters",permalink:"/docs/reference/count_chapters",editUrl:"https://github.com/avendesora/pythonbible/edit/main/pythonbible-docs/docs/reference/count_chapters.md",version:"current",sidebarPosition:8,frontMatter:{sidebar_position:8},sidebar:"tutorialSidebar",previous:{title:"count_books",permalink:"/docs/reference/count_books"},next:{title:"count_verses",permalink:"/docs/reference/count_verses"}},l=[{value:"Input",id:"input",children:[]},{value:"Output",id:"output",children:[]},{value:"Examples",id:"examples",children:[{value:"String Input Example",id:"string-input-example",children:[]},{value:"NormalizedReference Input Example",id:"normalizedreference-input-example",children:[]},{value:"List of NormalizedReferences Input Example",id:"list-of-normalizedreferences-input-example",children:[]}]}],p={toc:l};function s(e){var t=e.components,n=(0,o.Z)(e,["components"]);return(0,i.kt)("wrapper",(0,r.Z)({},p,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"count_chapters")," function, given a ",(0,i.kt)("inlineCode",{parentName:"p"},"string")," containing one or more Scripture references or a ",(0,i.kt)("inlineCode",{parentName:"p"},"NormalizedReference")," object or a ",(0,i.kt)("inlineCode",{parentName:"p"},"List")," of ",(0,i.kt)("inlineCode",{parentName:"p"},"NormalizedReference")," objects, returns the ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," count of the chapters included in the given reference(s)."),(0,i.kt)("h2",{id:"input"},"Input"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"count_chapters")," function accepts a single argument of one of the following three types:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"string")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"NormalizedReference")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("inlineCode",{parentName:"li"},"List[NormalizedReference]"))),(0,i.kt)("h2",{id:"output"},"Output"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"count_chapters")," function returns an ",(0,i.kt)("inlineCode",{parentName:"p"},"int")," greater than or equal to 0 that represents the number of chapters contained in the given reference(s)."),(0,i.kt)("h2",{id:"examples"},"Examples"),(0,i.kt)("h3",{id:"string-input-example"},"String Input Example"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\n# Genesis - Deuteronomy\nbible.count_chapters("Genesis has 50 chapters, but Exodus has 40.")\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"90\n")),(0,i.kt)("h3",{id:"normalizedreference-input-example"},"NormalizedReference Input Example"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\n# Matthew - John (i.e. bible.get_references("Matthew - John"))\nreference = bible.NormalizedReference(\n    book=bible.Book.MATTHEW,\n    start_chapter=1,\n    start_verse=1,\n    end_chapter=21,\n    end_verse=25,\n    end_book=bible.Book.JOHN\n)\nbible.count_chapters(reference)\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"89\n")),(0,i.kt)("h3",{id:"list-of-normalizedreferences-input-example"},"List of NormalizedReferences Input Example"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Code"',title:'"Code"'},'import pythonbible as bible\n\n# Genesis and Matthew - Acts (ie. bible.get_references("Genesis, Matthew - Acts"))\nreferences = [\n    bible.NormalizedReference(\n        book=bible.Book.GENESIS,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=50,\n        end_verse=26,\n        end_book=None\n    ),\n    bible.NormalizedReference(\n        book=bible.Book.MATTHEW,\n        start_chapter=1,\n        start_verse=1,\n        end_chapter=28,\n        end_verse=31,\n        end_book=bible.Book.ACTS\n    ),\n]\nbible.count_chapters(references)\n')),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="Result"',title:'"Result"'},"167\n")))}s.isMDXComponent=!0}}]);