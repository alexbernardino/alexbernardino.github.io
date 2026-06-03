require "bibtex"

file = ARGV[0] || "_bibliography/conferences.bib"
text = File.read(file)

entries = text.split(/\n(?=@)/)

entries.each_with_index do |entry, i|
  next if entry.strip.empty?

  begin
    BibTeX.parse(entry)
  rescue => e
    puts "Problem in entry #{i + 1}:"
    puts "-" * 60
    puts entry.lines.first(20).join
    puts "-" * 60
    puts e.message
    exit 1
  end
end

puts "BibTeX parsed successfully: #{entries.size} entries checked."

