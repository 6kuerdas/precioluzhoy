(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[332],{7276:(e,t,r)=>{(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return r(6993)}])},6993:(e,t,r)=>{"use strict";r.r(t),r.d(t,{Flex_9102a524832faa64789904dc1d775851:()=>Y,Flex_9bf276ee92dae8f221c2348c9ba59431:()=>m,Fragment_5dcdf44bc88617bd34c74764b26a5dcb:()=>x,Moment_8ab61f4bf250961da550f943f9a5a435:()=>g,Text_fd7986023a9d9ba303f0c9aa5a161caf:()=>f,default:()=>b});var a=r(2445),n=r(6540),c=r(9057),i=r(2996),s=r(9188),o=r(4953),l=r.n(o),d=r(2930);r(4743);var _=r(2225),p=r(3368),h=r.n(p);let u=l()(()=>r.e(300).then(r.t.bind(r,3300,23)),{loadableGenerated:{webpack:()=>[3300]},ssr:!1});function m(){var e;let t=(0,n.useContext)(s.StateContexts.reflex___state____state__render_prices____state);return(0,a.Y)(c.s,{align:"end",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.Y)(a.FK,{children:null===(e=t.today_prices)||void 0===e?void 0:e.prices.map((e,r)=>{var c,s;return(0,a.Y)(n.Fragment,{children:(0,d.isTrue)(t.clock_icon_list.at(r))?(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{color:"rgb"+(null===(c=t.today_prices)||void 0===c?void 0:c.colors.at(r)),whiteSpace:"nowrap",fontSize:"17px",fontWeight:"bold",animation:"thumbs 1.5s"},children:e+" €/kWh"})}):(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{color:"rgb"+(null===(s=t.today_prices)||void 0===s?void 0:s.colors.at(r)),whiteSpace:"nowrap"},children:e+" €/kWh"})})},r)})})})}function g(){let[e,t]=(0,n.useContext)(s.EventLoopContext),r=(0,n.useContext)(s.StateContexts.reflex___state____state__render_prices____state),c=(0,n.useCallback)(t=>e([(0,d.Event)("reflex___state____state.render_prices____state.update",{},{})],[t],{}),[e,d.Event]);return(0,a.Y)(u,{css:{color:"black"},format:"HH:mm:ss",interval:1e3,onChange:c,tz:"Europe/Paris",children:r.date_now})}function f(){let e=(0,n.useContext)(s.StateContexts.reflex___state____state__render_prices____state);return(0,a.Y)(i.E,{align:"center",as:"p",css:{fontSize:"20px",color:"black"},children:e.date})}function x(){var e;let t=(0,n.useContext)(s.StateContexts.reflex___state____state__render_prices____state),[r,o]=(0,n.useContext)(s.EventLoopContext);return(0,a.Y)(n.Fragment,{children:t.hide_tomorrow?(0,a.Y)(n.Fragment,{children:(0,a.Y)(c.s,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.FD)(c.s,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.Y)(i.E,{align:"center",as:"p",css:{fontSize:"20px",color:"black",marginTop:"10px"},children:"Precio de la luz ma\xf1ana"}),(0,a.Y)(u,{format:"HH:mm:ss",interval:1e3,onChange:e=>r([(0,d.Event)("reflex___state____state.render_prices____state.update",{},{})],[e],{}),tz:"Europe/Paris",children:t.date_now}),(0,a.Y)(i.E,{align:"center",as:"p",css:{fontSize:"12px",color:"black"},children:"Tarifa PVPC. Fuente: Red El\xe9ctrica Espa\xf1ola"}),(0,a.FD)(c.s,{align:"center",css:{background:"#edf9ff",minWidth:"350px",flexGrow:"3",padding:"30px",border:"2px solid #3498db",borderRadius:"12px",marginBottom:"30px"},justify:"between",children:[(0,a.Y)(c.s,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.Y)(a.FK,{children:["00:00 - 01:00","01:00 - 02:00","02:00 - 03:00","03:00 - 04:00","04:00 - 05:00","05:00 - 06:00","06:00 - 07:00","07:00 - 08:00","08:00 - 09:00","09:00 - 10:00","10:00 - 11:00","11:00 - 12:00","12:00 - 13:00","13:00 - 14:00","14:00 - 15:00","15:00 - 16:00","16:00 - 17:00","17:00 - 18:00","18:00 - 19:00","19:00 - 20:00","20:00 - 21:00","21:00 - 22:00","22:00 - 23:00","23:00 - 24:00"].map((e,r)=>{var s;return(0,a.FD)(c.s,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,a.Y)(_.A,{css:{color:"rgb"+(null===(s=t.tomorrow_prices)||void 0===s?void 0:s.colors.at(r))}}),(0,a.Y)(n.Fragment,{children:((0,d.isTrue)(t.clock_icon_list.at(r)),(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{whiteSpace:"nowrap",color:"black"},children:e})}))})]},r)})})}),(0,a.Y)(c.s,{align:"end",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.Y)(a.FK,{children:null===(e=t.tomorrow_prices)||void 0===e?void 0:e.prices.map((e,r)=>{var c,s;return(0,a.Y)(n.Fragment,{children:(0,d.isTrue)(t.clock_icon_list.at(r))?(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{color:"rgb"+(null===(c=t.tomorrow_prices)||void 0===c?void 0:c.colors.at(r)),whiteSpace:"nowrap"},children:e+" €/kWh"})}):(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{color:"rgb"+(null===(s=t.tomorrow_prices)||void 0===s?void 0:s.colors.at(r)),whiteSpace:"nowrap"},children:e+" €/kWh"})})},r)})})})]})]})})}):(0,a.Y)(n.Fragment,{})})}function Y(){let e=(0,n.useContext)(s.StateContexts.reflex___state____state__render_prices____state),t=(0,n.useRef)(null);return d.refs.ref_focus_item_id=t,(0,a.Y)(c.s,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:(0,a.Y)(a.FK,{children:["00:00 - 01:00","01:00 - 02:00","02:00 - 03:00","03:00 - 04:00","04:00 - 05:00","05:00 - 06:00","06:00 - 07:00","07:00 - 08:00","08:00 - 09:00","09:00 - 10:00","10:00 - 11:00","11:00 - 12:00","12:00 - 13:00","13:00 - 14:00","14:00 - 15:00","15:00 - 16:00","16:00 - 17:00","17:00 - 18:00","18:00 - 19:00","19:00 - 20:00","20:00 - 21:00","21:00 - 22:00","22:00 - 23:00","23:00 - 24:00"].map((r,s)=>{var o;return(0,a.FD)(c.s,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,a.Y)(_.A,{css:{color:"rgb"+(null===(o=e.today_prices)||void 0===o?void 0:o.colors.at(s))}}),(0,a.Y)(n.Fragment,{children:(0,d.isTrue)(e.clock_icon_list.at(s))?(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{whiteSpace:"nowrap",color:"black",fontWeight:"900",fontSize:"17px",animation:"thumbs 1.5s"},id:"focus_item_id",ref:t,children:r})}):(0,a.Y)(n.Fragment,{children:(0,a.Y)(i.E,{as:"p",css:{whiteSpace:"nowrap",color:"black"},children:r})})})]},s)})})})}function b(){return(0,a.FD)(n.Fragment,{children:[(0,a.FD)(c.s,{align:"center",className:"rx-Stack",css:{background:"white"},direction:"column",gap:"3",children:[(0,a.Y)(c.s,{align:"center",className:"rx-Stack",css:{background:"white"},direction:"column",gap:"3",children:(0,a.FD)(c.s,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:[(0,a.Y)(i.E,{align:"center",as:"p",css:{fontSize:"20px",color:"black",marginTop:"10px"},children:"Precio de la luz hoy"}),(0,a.Y)(f,{}),(0,a.Y)(g,{}),(0,a.Y)(i.E,{align:"center",as:"p",css:{fontSize:"12px",color:"black"},children:"Tarifa PVPC. Fuente: Red El\xe9ctrica Espa\xf1ola"}),(0,a.Y)(c.s,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,a.FD)(c.s,{align:"center",css:{background:"#edf9ff",minWidth:"350px",flexGrow:"3",padding:"30px",animation:"fadeDown 0.5s ease-in-out;",border:"2px solid #3498db",borderRadius:"12px",marginBottom:"30px"},justify:"between",children:[(0,a.Y)(Y,{}),(0,a.Y)(m,{})]}),(0,a.Y)(c.s,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}})]})}),(0,a.Y)(x,{})]}),(0,a.FD)(h(),{children:[(0,a.Y)("title",{children:"Precioluzhoy | Index"}),(0,a.Y)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},e=>{var t=t=>e(e.s=t);e.O(0,[90,197,482,636,593,792],()=>t(7276)),_N_E=e.O()}]);