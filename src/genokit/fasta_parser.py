from genokit.fasta import FastaRecord


'''
def parse_fasta(source) -> Iterator of FastaRecord:

    Open source as text stream
    line num = 0
    
    current_id = None
    current_description = None
    sequence_chunks = [] Empty list of strings

    header_found = false

    define flush_current_record(): (inner function)
        if current_id is None:
            return None
            
        raw_sequence = concatenate(sequence_chunks)
        clean_sequence = (remove whitespace)
        clean_sequence = (uppercase)
    
        record = FastaRecord(current_id,
                             current_description, 
                             clean_sequence)
    
        return record
    
    for each line in stream:
        line_num += 1
        line = line.rstrip("\r\n")
        
        if line is empty or contains only whitespace
            continue (ignore blank/whitespace only lines)
        
        if line starts with >
            header_found = true
            
            record = flush_current_record()
            if record !None:
                yield record
            
            header = line[1:].strip()
            if header is empty:
                raise ValueError("FASTA header missing ID at line)
                
            parts = header.split(maxsplit=1)
            current_id = parts[0]
            
            if len(parts) ==2:
                description = parts[1].strip()
                current_description = description if description != "" else None
            else:
                current_description = None
            
            sequence_chunks = []empty list
            continue
            
        if header_found == False
            raise ValueError FASTA sequence/data found before header at line#
            
        sequence_chunks.append(line)
       
    record = flush_current_record() - safety flush at end of script
    if record is not none:
        yield record

'''