import React from 'react';
import {useState, useEffect} from 'react';

const startTime = Date.now()

const StatusIndicator = ({color}) => {
    return(
        <div style={{display:'flex', alignItems:'center', gap:'3px'}}>
        <div className='small-circle'
            style={{
                width:'8px',
                height:'8px',
                backgroundColor:color,
                borderRadius: '50%'
            }}></div>
        <p> Engine Status</p>
        </div>
    );
};

const severityColors = {
    critical: '#A32D2D',
    high: '#854F0B',
    medium: '#185FA5',
    low: '#3B6D11'
}

function Clock(){
    const [time, setTime] = useState("00:00:00")
    useEffect(() => {
        const interval = setInterval(()=>{
            setTime(new Date().toLocaleTimeString())
        }, 1000)
        return() => clearInterval(interval)
    }, [])
    return(
        <div>
            <p>{time}</p>
        </div>
    );
};


function Topbar(){
    return(
        <div style={{display:'flex', justifyContent:'space-between'}}>
            <div> 
            <div style={{fontSize:'32px', fontWeight:'500'}}>Threat Sentinel</div>
            <div style={{fontSize:'20px', color:'#64748b'}}>Host Intrusion Detection System</div>
            </div>
            <div style={{display:'flex', alignItems:'center', gap:'16px'}}><StatusIndicator color='green'/>
            <Clock/>
            </div>
        </div>
    );
}
const MetricCard = ({label, value, color}) =>{
    return(
        <div style={{flex:1, padding:'14px 16px', border:'1px solid #2a2d3a',background:'#1a1d27', borderRadius:'8px'}}>
            <p style={{color:'#64748b'}}>{label} </p>
            <p style={{fontSize:'24px', fontWeight:'500', color:color}}>{value}</p>
        </div>
    );
};

function Metrics({totalThreats, critical, blocked, rate}){
    return(
        <div style={{display:'flex', alignItems:'center', gap:'10px'}}>
            <MetricCard label="Total Threats" value={totalThreats} color="#E24B4A"/>
            <MetricCard label="Critical" value={critical} color="#EF9F27"/>
            <MetricCard label="Blocked" value={blocked} color="#639922"/>
            <MetricCard label="Detection Rate" value={rate} color="#378ADD"/>
        </div>
    );
}

function ThreatRow({threat}){
    return(
        <div style={{display:'flex', gap:'16px', padding:'10px 16px', borderBottom:'1px solid #2a2d3a'}}>
            <span style={{color: severityColors[threat.severity]}}>{threat.severity}</span>
            <span>{threat.name}</span>
            <span>{threat.source}</span>
        </div>
    );
}
function SystemLog({logs}){
    return(
        <div style = {{border:'1px solid #2a2d3a',background:'#1a1d27', borderRadius:'8px',
                        maxHeight:'400px', overflowY:'scroll', padding:'8px'}}>
            {logs.map((log, index) => (
                <div key={index} style={{fontSize:'11px', padding:'4px 8px',
                            color:'#666', borderBottom:'1px solid #f0f0f0'}}>
                    <span style={{color:'#999', marginRight:'8px'}}>
                        {new Date(log.timestamp * 1000).toLocaleTimeString()}
                    </span>
                    {log.message}
                </div>
            ))}
        </div>
    );
}
function MContent({threats, logs}){
    return(
        <div style={{display:'flex', gap:'14px'}}>
            <div style={{flex: 2, border:'1px solid #2a2d3a', borderRadius:'8px', overflow:'hidden', maxHeight:'400px', overflowY:'scroll'}}>    
                {threats.length === 0
                    ? <div style={{padding:'2rem', textAlign:'center', color:'#64748b'}}>
                        No threats detected. Monitoring...
                      </div>  
                    :threats.map(threat => (
                        <ThreatRow key={threat.id} threat={threat} />
                    ))
                }
            </div>
            <div style={{flex:1}}>
                <SystemLog logs = {logs}/>
            </div>
        </div>
    );
}
function App(){
    const [totalThreats, setTotalThreats] = useState(0)
    const [critical, setCritical] = useState(0)
    const [blocked, setBlocked] = useState(0)
    const [rate, setRate] = useState(0)
    const [threats, setThreats] = useState([])
    const [logs, setLogs] = useState([])
    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8000/ws')
        ws.onmessage = (event) => {
            const msg = JSON.parse(event.data)
            if(msg.type === 'threat'){
                const threat = {...msg.data, id: Date.now()}
                setThreats(prev => [threat, ...prev])
                setTotalThreats(prev => {
                    const newTotal = prev + 1
                    if(threat.severity === 'critical') setCritical(prev => prev + 1)
                    setRate(Math.round(newTotal/ ((Date.now()-startTime)/60000)))
                    return newTotal
                })
            }
            if(msg.type === 'log'){
                setLogs(prev => [msg, ...prev])
            }
            
            }
        return() => ws.close()
}, [])
    return(
        <div style={{display:'flex', flexDirection:'column', gap:'16px'}}>
            <Topbar />
            <Metrics totalThreats={totalThreats} critical={critical} blocked={blocked} rate={rate}/>
            <MContent threats={threats} logs={logs}/>
        </div>
    );
}

export default App;
