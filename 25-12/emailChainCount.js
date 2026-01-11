function emailChainCount(subject) {
  return (subject.match(/\b(?:re|fw|fwd):/gi) || []).length
}

console.log(emailChainCount("re:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary"))